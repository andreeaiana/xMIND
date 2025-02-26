<div align="center">

# xMIND
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

</div>

# Description

xMIND is a large-scale multilingual news dataset for multi- and cross-lingual news recommendation. xMIND is derived from the English [MIND](https://msnews.github.io/assets/doc/ACL2020_MIND.pdf) (https://msnews.github.io/) dataset using open-source neural machine translation (i.e., [NLLB](https://arxiv.org/pdf/2207.04672.pdf) 3.3B). xMIND contains 130K news translated into 14 linguistically and geographically diverse languages, with digital footprints of varying sizes. The goal of xMIND is to serve as a benchmark dataset for news recommendation, and to foster broader research into multilingual and cross-lingual news recommendation, for speakers of both high and low-resource languages.

The table below summarizes information about each language included in xMIND, according to the following criteria:
- **Code**: the three-letter ISO 693-3 code of the language;
- **Language**: the language name from [WALS](https://wals.info/languoid);
- **Script**: the English name of the script;
- **Macro-area**, **Family** ,and **Genus**: the macro-area, language family and genus from [WALS](https://wals.info/languoid) and [Glottolog](https://glottolog.org/)
- **Res.**: the classification from [](https://arxiv.org/pdf/2207.04672.pdf) into _low-resource_ and _high-resource_

| **Code** 	                | **Language**     	| **Script** 	| **Macro-area** 	| **Family**     	| **Genus**             	| **Res.** 	|
|--------------------------	|------------------	|------------	|----------------	|----------------	|-----------------------	|----------	|
| [SWH](./xMIND/swh/)      	| Swahili          	| Latin      	| Africa         	| Niger-Congo    	| Bantu                 	| high     	|
| [SOM](./xMIND/som/)      	| Somali           	| Latin      	| Africa         	| Afro-Asiatic   	| Lowland East Cushitic 	| low      	|
| [CMN](./xMIND/cmn/)      	| Mandarin Chinese 	| Han        	| Eurasia        	| Sino-Tibetan   	| Sinitic               	| high     	|
| [JPN](./xMIND/jpn/)      	| Japanese         	| Japanese   	| Eurasia        	| Japonic        	| Japanesic             	| high     	|
| [TUR](./xMIND/tur/)      	| Turkish          	| Latin      	| Eurasia        	| Altaic         	| Turkic                	| high     	|
| [TAM](./xMIND/tam/)      	| Tamil            	| Tamil      	| Eurasia        	| Dravidian      	| Dravidian             	| low      	|
| [VIE](./xMIND/vie/)      	| Vietnamese       	| Latin      	| Eurasia        	| Austro-Asiatic 	| Vietic                	| high     	|
| [THA](./xMIND/tha/)      	| Thai             	| Thai       	| Eurasia        	| Tai-Kadai      	| Kam-Tai               	| high     	|
| [RON](./xMIND/ron/)      	| Romanian         	| Latin      	| Eurasia        	| Indo-European  	| Romance               	| high     	|
| [FIN](./xMIND/fin/)      	| Finnish          	| Latin      	| Eurasia        	| Uralic         	| Finnic                	| high     	|
| [KAT](./xMIND/kat/)      	| Georgian         	| Georgian   	| Eurasia        	| Kartvelic      	| Georgian-Zan          	| low      	|
| [HAT](./xMIND/hat/)      	| Haitian Creole   	| Latin      	| North-America  	| Indo-European  	| Creoles and Pidgins   	| low      	|
| [IND](./xMIND/ind/)      	| Indonesian       	| Latin      	| Papunesia      	| Austronesian   	| Malayo-Sumbawan       	| high     	|
| [GRN](./xMIND/grn/)      	| Guarani          	| Latin      	| South-America  	| Tupian         	| Maweti-Guarani        	| low      	|

# Download
The xMIND dataset is free to download for research purposes. 

We release the xMIND in two versions, corresponding to the original splits of [MIND]((https://msnews.github.io/)): **xMINDsmall** (training and validation sets) and **xMINDlarge** (training, validation, and test sets). 

The zip-compressed TSV file containing the translated news, for each language and each split, can be downloaded from [xMIND](xMIND/).

## Automatically download

The [download script](./download.py) enables automatically downloading the dataset for the chosen _language_, _dataset size_, and _dataset split_. 
By _default_, the scripts downloads the zipped dataset, extracts the TSV news file, and deletes the zip file. 

The following commands can be used to choose which dataset version to dowload:

- Download xMIND for **all** languages, **all** dataset sizes, **all** dataset splits (default setting):
    ```python
        python download.py
    ```

- Download only one or more languages:
    ```python
        python download.py --languages {language_1} {language_2}
    ```
    Use the ISO 693-3 code of the language from the table above to choose a specific language. 

- Download only one or more dataset sizes:
    ```python
        python download.py --sizes {dataset_size_1} {dataset_size_2}
    ```
    Supported dataset sizes: _large_ or _small_.

- Download only one or more dataset splits:
    ```python
        python download.py --splits {dataset_split_1} {dataset_split_2} {dataset_split_3}
    ```
    Supported dataset splits: _train_, _dev_, or _test_.

- Download without extracting the zipped file:
    ```python
        python download.py --extract_archive 
    ```
- Download without deleting the zipped file:
    ```python
        python download.py --clean_archive 
    ```

- The downloaded dataset is by default stored in a newly created directory called _xmIND_. Change the destination directory as follows:
    ```python
        python download.py --dst_dir 'my_folder' 
    ```


## Data Format
Each _news.tsv_ file contains the translated news; it has 3 columns, separated by the tab symbol:
- nid: News ID of the article, identical to the corresponding news ID from the MIND dataset of the article.
- title: The title of the news translated into the target language.
- abstract: The abstract of the news (when provided in the original MIND dataset) translated into the target language.  

An example for Romanian (RON) is shown below:

| **nid** 	| **title**                                                                      	| **abstract**                                               	|
|---------	|--------------------------------------------------------------------------------	|------------------------------------------------------------	|
| N49265  	| Aceste reţete cu sos de afine sunt perfecte pentru cina de Ziua Recunoştinţei. 	| Nu vei mai vrea niciodată versiunea cumpărată din magazin. 	|


# Integration with MIND
The news in xMIND can be easily combined with the corresponding source news in English from the MIND dataset based on the unique news IDs. This should help researchers use xMIND in conjunction with the additional news annotations (e.g., categories, subcategories, named entities) and user behavior information provided in MIND.

To facilitate a seamless integration of xMIND with the MIND data, we provide scripts for loading the dataset and constructing bilingual user consumption patterns in the [NewsRecLib](https://github.com/andreeaiana/newsreclib/tree/main) library.

# License
This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

If you intend to use, adapt, or share xMIND, particularly together with additional news and click behavior information from the original MIND dataset, please read and reference the [Microsoft Research License Terms](https://github.com/msnews/MIND/blob/master/MSR%20License_Data.pdf) of MIND.

## Citation

If you use xMIND, please cite the following publication:

```
@misc{iana2024mind,
      title={MIND Your Language: A Multilingual Dataset for Cross-lingual News Recommendation}, 
      author={Andreea Iana and Goran Glavaš and Heiko Paulheim},
      year={2024},
      eprint={2403.17876},
      archivePrefix={arXiv},
      primaryClass={cs.IR}
}
```

Also consider citing the following:
```
@inproceedings{wu2020mind,
  title={Mind: A large-scale dataset for news recommendation},
  author={Wu, Fangzhao and Qiao, Ying and Chen, Jiun-Hung and Wu, Chuhan and Qi, Tao and Lian, Jianxun and Liu, Danyang and Xie, Xing and Gao, Jianfeng and Wu, Winnie and others},
  booktitle={Proceedings of the 58th annual meeting of the association for computational linguistics},
  pages={3597--3606},
  year={2020}
}
```