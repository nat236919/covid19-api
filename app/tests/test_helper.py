"""
FILE: test_helper.py
DESCRIPTION: Test helper functions
AUTHOR: Nuttaphat Arunoprayoch
DATE: 02-Sep-2020
"""
# Import libraries
import pandas as pd
from ..utils import helper
from ..utils.file_paths import JHUCSSEDatasetURL


# Test DataFrame
DATA = {'col_1': list(range(5)), 'col_2': [1, None, '', None, None]}
DF = pd.DataFrame(DATA)


# Test df cleaning
def test_helper_df_cleaning() -> None:
    df = DF.copy()
    res_df = helper.helper_df_cleaning(df)
    res_col_1 = [i for i in res_df['col_1'].values]
    res_col_2 = [i for i in res_df['col_2'].values]
    assert isinstance(res_df, pd.DataFrame) is True
    assert res_col_1 == [i for i in DF['col_1'].values]
    assert res_col_2 == [1, '', '', '', '']


# Test df cleaning on columns
def test_helper_df_cols_cleaning() -> None:
    df = DF.copy()
    res_df = helper.helper_df_cols_cleaning(df, ['col_2'], str)
    res_col_1 = [i for i in res_df['col_1'].values]
    res_col_2 = [i for i in res_df['col_2'].values]
    assert isinstance(res_df, pd.DataFrame) is True
    assert res_col_1 == [i for i in DF['col_1'].values]
    assert res_col_2 != [i for i in DF['col_2'].values]
