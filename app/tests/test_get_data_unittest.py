"""
FILE: test_get_data_unittest.py
DESCRIPTION: Test reading raw files from GitHub
AUTHOR: Quang Hy Le
DATE: 18-April-2021
"""
# Import libraries
import pandas as pd
import unittest

from ..utils.get_data import (DailyReports, DataTimeSeries)


class GetDataDailyReportsTest(unittest.TestCase):
    daily_reports = DailyReports()
    data = daily_reports.get_data_daily_reports()

    # Test - Get data from daily reports
    def test_instance(self) -> None:
        self.assertTrue(isinstance(self.data, pd.DataFrame))

    def test_number_columns(self) -> None:
        self.assertEqual(len(self.data.columns), 4)

    def test_first_columns(self) -> None:
        self.assertEqual(self.data.columns[0], 'Confirmed')

    def test_second_columns(self) -> None:
        self.assertEqual(self.data.columns[1], 'Deaths')

    def test_third_columns(self) -> None:
        self.assertEqual(self.data.columns[2], 'Recovered')

    def test_fourth_columns(self) -> None:
        self.assertEqual(self.data.columns[3], 'Active')


if __name__ == '__main__':
    pass
