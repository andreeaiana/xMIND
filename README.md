<div align="center">

# xMIND

</div>

# Description

xMIND is a large-scale multilingual news dataset for multi- and cross-lingual news recommendation. xMIND is derived from the English [MIND](https://msnews.github.io/assets/doc/ACL2020_MIND.pdf) (https://msnews.github.io/) dataset using open-source neural machine translation (i.e., [NLLB](https://arxiv.org/pdf/2207.04672.pdf) 3.3B). xMIND contains 130K news translated into 14 linguistically and geographically diverse languages, with digital footprints of varying sizes. The goal of xMIND is to serve as a benchmark dataset for news recommendation, and to foster broader research into multilingual and cross-lingual news recommendation, for speakers of both high and low-resource languages.

The table below summarizes information about each language included in xMIND, according to the following criteria:
- **Code**: the three-letter ISO 693-3 code of the language;
- **Language**: the language name from [WALS](https://wals.info/languoid);
- **Script**: the English name of the script;
- **Macro-area**, **Family** ,and **Genus**: the macro-area, language family and genus from [WALS](https://wals.info/languoid) and [Glottolog](https://glottolog.org/)
- **Res.**: the classification from [](https://arxiv.org/pdf/2207.04672.pdf) into _low-resource_ and _high-resource_

| **Code** 	| **Language**     	| **Script** 	| **Macro-area** 	| **Family**     	| **Genus**             	| **Res.** 	|
|----------	|------------------	|------------	|----------------	|----------------	|-----------------------	|----------	|
| SWH      	| Swahili          	| Latin      	| Africa         	| Niger-Congo    	| Bantu                 	| high     	|
| SOM      	| Somali           	| Latin      	| Africa         	| Afro-Asiatic   	| Lowland East Cushitic 	| low      	|
| CMN      	| Mandarin Chinese 	| Han        	| Eurasia        	| Sino-Tibetan   	| Sinitic               	| high     	|
| JPN      	| Japanese         	| Japanese   	| Eurasia        	| Japonic        	| Japanesic             	| high     	|
| TUR      	| Turkish          	| Latin      	| Eurasia        	| Altaic         	| Turkic                	| high     	|
| TAM      	| Tamil            	| Tamil      	| Eurasia        	| Dravidian      	| Dravidian             	| low      	|
| VIE      	| Vietnamese       	| Latin      	| Eurasia        	| Austro-Asiatic 	| Vietic                	| high     	|
| THA      	| Thai             	| Thai       	| Eurasia        	| Tai-Kadai      	| Kam-Tai               	| high     	|
| RON      	| Romanian         	| Latin      	| Eurasia        	| Indo-European  	| Romance               	| high     	|
| FIN      	| Finnish          	| Latin      	| Eurasia        	| Uralic         	| Finnic                	| high     	|
| KAT      	| Georgian         	| Georgian   	| Eurasia        	| Kartvelic      	| Georgian-Zan          	| low      	|
| HAT      	| Haitian Creole   	| Latin      	| North-America  	| Indo-European  	| Creoles and Pidgins   	| low      	|
| IND      	| Indonesian       	| Latin      	| Papunesia      	| Austronesian   	| Malayo-Sumbawan       	| high     	|
| GRN      	| Guarani          	| Latin      	| South-America  	| Tupian         	| Maweti-Guarani        	| low      	|

# Download
The xMIND dataset is free to download for research purposes. 

We release the xMIND in two versions, corresponding to the original splits of [MIND]((https://msnews.github.io/)): **xMINDsmall** (training and validation sets) and **xMINDlarge** (training, validation, and test sets). 

The zip-compressed TSV file containing the translated news, for each language and each split, can be downloaded from [xMIND](xMIND/).

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

