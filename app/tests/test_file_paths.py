"""
FILE: test_file_paths.py
DESCRIPTION: Test URL generating class for API
AUTHOR: Jerry Chen
DATE: 17-Mar-2021
"""
# Import libraries
from ..utils.file_paths import JHUCSSEDatasetURL

# Test get latest data
def test_helper_get_latest_data_url() -> None:
    assert isinstance(JHUCSSEDatasetURL.get_lookup_table_url(), str)
    assert isinstance(JHUCSSEDatasetURL.get_daily_report_url(), str)
    assert isinstance(JHUCSSEDatasetURL.get_daily_report_us_url(), str)
    ## Temporily disable timeseries testing
    # assert isinstance(JHUCSSEDatasetURL.get_time_series_url(), str)
    # assert isinstance(JHUCSSEDatasetURL.get_time_series_us_url(), str)

