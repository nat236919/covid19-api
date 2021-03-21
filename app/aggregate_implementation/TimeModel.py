"""
FILE:TimeModel.py
DESCRIPTION: Encapsulation of all data
AUTHOR: Ka Hei Chan
DATE: 17-March-2021
"""

import time


class TimeModel:
    TimeStamp: int
    Date: str
    Year: int
    Day: int
    Month: int

    def __init__(self, date: str, ts: int) -> None:
        self.Date = date
        self.TimeStamp = ts
        date_digit = int(date.split("/"))
        self.Day = date_digit[0]
        self.Month = date_digit[1]
        self.Year = date_digit[2]

    def get_year(self):
        return self.Year

    def get_date(self):
        return self.Date

    def get_month(self):
        return self.Month

    def get_timestamp(self):
        return self.TimeStamp
