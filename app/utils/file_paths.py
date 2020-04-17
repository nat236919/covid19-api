"""
FILE: file_paths.py
DESCRIPTION: Keep file paths from the data source
AUTHOR: Nuttaphat Arunoprayoch
DATE: 17-April-2020
"""
# Johns Hopkins CSSE - Datasets (https://github.com/CSSEGISandData/COVID-19)
JHU_CSSE_DAILY_REPORT_PATH = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'
JHU_CSSE_TIME_SERIES_PATH = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'
JHU_CSSE_LOOKUP_TABLE_PATH = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv'
JHU_CSSE_CATEGORIES = ['confirmed', 'deaths', 'recovered']

JHU_CSSE_FILE_PATHS = {
    'BASE_URL_LOOKUP_TABLE': JHU_CSSE_LOOKUP_TABLE_PATH,
    'BASE_URL_DAILY_REPORTS': JHU_CSSE_DAILY_REPORT_PATH + '{}.csv',
    'BASE_URL_TIME_SERIES': JHU_CSSE_TIME_SERIES_PATH + 'time_series_covid19_{}_global.csv',
    'BASE_URL_US_TIME_SERIES': JHU_CSSE_TIME_SERIES_PATH + 'time_series_covid19_{}_US.csv',
    'CATEGORIES': JHU_CSSE_CATEGORIES
}
