"""
FILE: test_get_data.py
DESCRIPTION: Test reading raw files from GitHub
AUTHOR: Nuttaphat Arunoprayoch
DATE: 11-April-2020
"""
# Import libraries
import pandas as pd
from ..utils.get_data import COVIDDataForAPIv1, COVIDDataForAPIv2, get_data_lookup_table
from ..utils import file_paths 

# Test DataFrame
DATA = {'col_1': list(range(5)), 'col_2': [1, None, '', None, None]}
DF = pd.DataFrame(DATA)

# Test - Get Lookup table
def test_get_data_lookup_table() -> None:
    result = get_data_lookup_table()
    assert len(result) > 0
    assert isinstance(result, dict) is True


# Test - Get data from daily reports
def test_get_data_daily_reports() -> None:
    result = COVIDDataForAPIv2.get_data_daily_reports()
    assert len(result) > 0
    assert isinstance(result, pd.DataFrame) is True 


# Test - Get data from daily reports (US)
def test_get_data_daily_reports_US() -> None:
    result = COVIDDataForAPIv2.get_data_daily_reports(US=True)
    assert len(result) > 0
    assert isinstance(result, pd.DataFrame) is True 


# Test - Get data from time series
def test_get_data_time_series() -> None:
    result = COVIDDataForAPIv2.get_data_time_series()
    assert len(result) > 0
    assert isinstance(result, dict) is True


# Test - Get data from time series (US)
def test_get_US_time_series() -> None:
    result = COVIDDataForAPIv2.get_US_time_series()
    assert len(result) > 0
    assert isinstance(result, dict) is True


# Test - Get Data (API v1)
def test_get_data() -> None:
    result = COVIDDataForAPIv1.get_data()
    assert len(result) > 0
    assert isinstance(result, dict) is True


# Test - Get Data (API v1)
def test_get_data(time_series = True) -> None:
    result = COVIDDataForAPIv1.get_data()
    assert len(result) > 0
    assert isinstance(result, dict) is True


# Test df cleaning
def test_helper_df_cleaning() -> None:
    df = DF.copy()
    res_df = COVIDDataForAPIv2._df_cleaning(df)
    res_col_1 = [i for i in res_df['col_1'].values]
    res_col_2 = [i for i in res_df['col_2'].values]
    assert isinstance(res_df, pd.DataFrame) is True
    assert res_col_1 == [i for i in DF['col_1'].values]
    assert res_col_2 == [1, '', '', '', '']


# Test df cleaning on columns
def test_helper_df_cols_cleaning() -> None:
    df = DF.copy()
    res_df = COVIDDataForAPIv2._df_cols_cleaning(df, ['col_2'], str)
    res_col_1 = [i for i in res_df['col_1'].values]
    res_col_2 = [i for i in res_df['col_2'].values]
    assert isinstance(res_df, pd.DataFrame) is True
    assert res_col_1 == [i for i in DF['col_1'].values]
    assert res_col_2 != [i for i in DF['col_2'].values]


# Test get latest data
def test_helper_get_latest_data_url() -> None:
    assert isinstance(COVIDDataForAPIv2._get_latest_data_url(file_paths.JHU_CSSE_FILE_PATHS['BASE_URL_LOOKUP_TABLE']), str)
    assert isinstance(COVIDDataForAPIv2._get_latest_data_url(file_paths.JHU_CSSE_FILE_PATHS['BASE_URL_DAILY_REPORTS']), str)
    assert isinstance(COVIDDataForAPIv2._get_latest_data_url(file_paths.JHU_CSSE_FILE_PATHS['BASE_URL_DAILY_REPORTS_US']), str)
    ## Temporily disable timeseries testing
    # assert isinstance(COVIDDataForAPIv2._get_latest_data_url(file_paths.JHU_CSSE_FILE_PATHS['BASE_URL_TIME_SERIES']), str)
    # assert isinstance(COVIDDataForAPIv2._get_latest_data_url(file_paths.JHU_CSSE_FILE_PATHS['BASE_URL_US_TIME_SERIES']), str)
