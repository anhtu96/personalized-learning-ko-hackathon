# Personalized Learning - Social Challenge (Kambria Online Hackathon 2021)

### Usage
1. Install Python packages

    ```pip install -r requirements.txt```

2. Merge seperated EdNet csv files into one file

    Download EdNet data from [this repo](https://github.com/riiid/ednet) and extract the zipped file into [datasets](/datasets). Run this command to merge the dataset: ```python -m merge_csv --dataset DATASET ```.
    
    DATASET can either be:
    - ```all```: merge KT1, KT2, KT3, KT4 sequentially.
    - ```KT1```, ```KT2```, ```KT3``` or ```KT4```: merge only one of these dataset each time. 