"""
FILE: helper.py
DESCRIPTION: Download and Unzip the data
AUTHOR: Nuttaphat Arunoprayoch
DATE: 9-Feb-2020
"""
# Import libraries
import kaggle
import zipfile
import pandas as pd


def get_data() -> pd.DataFrame:
    """ Get the dataset from Kaggle """
    # Download the dataset
    URL = 'sudalairajkumar/novel-corona-virus-2019-dataset'
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(URL, 'data')

    # Extract the file
    with zipfile.ZipFile('data/novel-corona-virus-2019-dataset.zip', 'r') as f:
        f.extractall('data')

    return pd.read_csv('data/2019_nCoV_data.csv')
