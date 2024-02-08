import os
import math
import zipfile
import argparse
import requests
from retrying import retry
from tqdm import tqdm

BASE_URL = 'https://github.com/andreeaiana/xMIND/raw/main/xMIND/'
xMIND_LANGUAGES = [
        'cmn',
        'fin', 
        'grn',
        'hat',
        'ind',
        'jpn',
        'kat',
        'ron',
        'som',
        'swh',
        'tam',
        'tha',
        'tur',
        'vie'
        ]
xMIND_SIZE_SPLIT_DICT = {
        'large': ['train', 'dev', 'test'],
        'small': ['train', 'dev']
        }

@retry(wait_random_min=1000, wait_random_max=5000, stop_max_attempt_number=5)
def download_file(
        url: str,
        filename: str,
        output_dir: str
        ) -> str:

    filepath = os.path.join(output_dir, filename) 
    
    r = requests.get(url, stream=True, timeout=10)
    if r.status_code == 200:
        print(f'Dowloading {url}')
        total_size = int(r.headers.get('content-length', 0))
        block_size=1024
        num_iterables = math.ceil(total_size / block_size)

        with open(filepath, 'wb') as f:
            for data in tqdm(
                    r.iter_content(block_size),
                    total=num_iterables,
                    unit='KB',
                    unit_scale=True
                    ):
                f.write(data)
    else:
        print(f'problem dowloading {url}')
        r.raise_for_status()

    return filepath


def extract_file(
        archive_file: str,
        dst_dir: str, 
        clean_archive: bool 
        ) -> None:
    print(f'Extracting {archive_file}.\n')
    fz = zipfile.ZipFile(archive_file, 'r')
    for file in fz.namelist():
        fz.extract(file, dst_dir)
    if clean_archive:
        os.remove(archive_file)


def main():
    parser = argparse.ArgumentParser(
            description='Download script arguments')
    
    # define arguments
    parser.add_argument(
            '--languages',
            nargs='*',
            dest='languages',
            default=[],
            required=False,
            help='The language for which to download the dataset. If not specified, it defaults to downloading the dataset for all languages.'
            )
    parser.add_argument(
            '--sizes',
            nargs='*',
            dest='sizes',
            default=[],
            required=False,
            help='The size of the dataset. If not specified, it defaults to downloding both the "large" and the "small" versions.'
            )
    parser.add_argument(
            '--splits',
            nargs='*',
            dest='splits',
            default=[],
            required=False,
            help='The dataset split. If not specified, it defaults to downloading all splits that exist for the chosen dataset.'
            )
    parser.add_argument(
            '--extract_archive',
            action='store_false',
            default=True,
            dest='extract_archive',
            help='Whether to extract the TSV file from the compressed archive. Defaults to True.'
            )
    parser.add_argument(
            '--clean_archive',
            action='store_false',
            default=True,
            dest='clean_archive',
            help='Whether to delete the compressed archive after extracting its files. Defaults to True.'
            )
    parser.add_argument(
            '--dst_dir',
            default='xMIND',
            dest='dst_dir',
            help='The location of the downloaded dataset. If not specified, it defaults to "xMIND".'
            )

    # parse arguments
    args = parser.parse_args()
    languages = args.languages
    sizes = args.sizes
    splits = args.splits
    extract_archive = args.extract_archive
    clean_archive = args.clean_archive
    dst_dir = args.dst_dir

    # languages
    if not languages:
        # no language selected, default to downloading the dataset for all languages
        languages = xMIND_LANGUAGES
    else:
        # validate that the selected languages exists
        for lang in languages:
            assert lang in xMIND_LANGUAGES

    # dataset sizes
    if not sizes:
        # no dataset size selected, default to downloading the dataset sizes
        sizes = xMIND_SIZE_SPLIT_DICT.keys()
    else:
        # validate that the selected size exists
        for size in sizes:
            assert size in xMIND_SIZE_SPLIT_DICT

    # dataset splits
    splits_per_size = {}
    if not splits:
        # no dataset size selected, default to downloading the dataset sizes
        for size in sizes:
            splits_per_size[size] = xMIND_SIZE_SPLIT_DICT[size]
    else:
        for size in sizes:
            splits_per_size[size] = [split for split in splits if split in xMIND_SIZE_SPLIT_DICT[size]]

    # download dataset
    print('Starting download.')
    for lang in languages:
        lang_dir = os.path.join(dst_dir, lang)
        os.makedirs(lang_dir, exist_ok=True)
        for size in sizes:
            for split in splits_per_size[size]:
                filename = 'xMIND' + size + '_' + split
                zipped_filename = filename + '.zip'
                url = BASE_URL + '/' + lang + '/' + zipped_filename 
                zipped_file = download_file(url=url, filename=zipped_filename, output_dir=lang_dir)
                if extract_archive:
                    extract_file(archive_file=zipped_file, dst_dir=lang_dir, clean_archive=clean_archive)
    print('Finished.')

if __name__ == "__main__":
    main()

