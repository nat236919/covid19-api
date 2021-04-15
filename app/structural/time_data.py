"""
FILE: time-data.py
AUTHOR: Vivian Dcruze
DATE: 14-April-2021
"""

import time

class TimeData:
    Date: str
    Timestamp: int
    Day: int
    Month: int
    Year: int
    TimeSince1970: int

    def __init__(self, date: str, timestamp: int) -> None:
        self.Date = date
        self.Timestamp = timestamp
        parsed_date = date.split("/")
        self.Day = parsed_date[0]
        self.Month = parsed_date[1]
        self.Year = parsed_date[2]
        self.TimeSince1970 = int(time.mktime(time.strptime(date, '%d.%m.%Y')))

    def get_Date:
        return self.Date

    def get_Timestamp
        return self.Timestamp
    
    def get_Day
        return self.Day

    def get_Month
        return self.Month

    def get_Year
        return self.Year

    def get_TimeSince1970
        return self.TimeSince1970