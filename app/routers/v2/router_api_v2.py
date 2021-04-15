import datetime
import json
import logging
import os
import re

import dateutil
import numpy as np
import pandas as pd

__CWD__ = os.path.abspath(os.path.dirname(__file__))

logging.basicConfig()
logger = logging.getLogger('cleansing.full')
logger.setLevel(logging.INFO)

GEO_COLS = ['country','nuts_1', 'nuts_2', 'nuts_3', 'lau']

class Wrangler:
    def __init__(self, csv_path, json_path):
        super().__init__()
        self.csv_path = csv_path
        self.json_path = json_path

        self.df = self._load_data()

        self.calculate_daily()
        self.convert_to_json()

    def _load_data(self):
        df = pd.read_csv(self.csv_path)
        return df

    def calculate_daily(self):
        self.df['date'] = self.df.datetime.apply(lambda x: dateutil.parser.parse(x).date())
        self.df['time'] = self.df.datetime.apply(lambda x: dateutil.parser.parse(x).time())

        cols = self.df.columns.tolist()
        geo_cols = []
        for col in cols:
            if col in GEO_COLS:
                geo_cols.append(col)

        if not geo_cols:
            raise Exception(f'No geo columns found among {cols}')

        for col in geo_cols:
            self.df[col] = self.df[col].apply(
                lambda x: x.lower() if (
                    (not pd.isnull(x)) and (isinstance(x, str))
                ) else x
            )
        self.df_daily = self.df.groupby(
            ['date'] + geo_cols
        ).apply(
            lambda x: x.sort_values(by='time').reset_index(drop=True).iloc[-1]
        )

        self.df_daily.reset_index(drop=True, inplace=True)
        self.df_daily.drop('time', inplace=True, axis=1)

        logger.debug('Calculated daily data')

    def convert_to_json(self):

        df = self.df_daily.copy()
        df.replace({np.nan:None}, inplace=True)
        logger.debug("Convert date to isoformat")
        df['date'] = df.date.apply(
            lambda x: x.isoformat() if isinstance(x, (datetime.date)) else x
        )
        logger.debug('Get country date combinations')
        country_dates = df[['country', 'date']].drop_duplicates().values

        self.data = []
        for i in country_dates:
            i_records = df.loc[
                (
                    df.country == i[0]
                ) & (
                    df.date == i[1]
                )
            ].to_dict(orient='records')

            self.data.append(
                {
                    "country": i[0],
                    "date": i[1],
                    "records": i_records
                }
            )

    def save_json(self):
        with open(self.json_path, 'w+') as fp:
            json.dump(self.data, fp)


def get_datasets(dataset_path):

    re_find_country = re.compile(r'covid-19-(.*).csv')

    files = os.listdir(dataset_path)

    files_full = {
        re_find_country.findall(i)[0]:i for i in files if (i.endswith('.csv') and not i.startswith('.'))
    }

    daily_path = os.path.join(dataset_path, 'daily')
    daily_countries = [
        i for i in os.listdir(
            daily_path
        ) if not i.startswith('.')
    ]

    files_daily = {}

    for i in daily_countries:
        i_path = os.path.join(daily_path, i)
        i_files = os.listdir(i_path)
        i_files = [os.path.join('daily', i, f) for f in i_files if not f.startswith('.')]
        files_daily[i] = i_files

    return {
        'full': files_full,
        'daily': files_daily
    }




if __name__ == "__main__":

    dataset_path = os.path.join(__CWD__, '..', 'dataset')
    db_path = os.path.join(__CWD__, '..', 'api', 'db')

    dataset = get_datasets(dataset_path)

    logger.info('Convert csv to json')
    for ct, path in dataset['full'].items():
        logger.info(f'cleaning up {ct}')
        csv_path = os.path.join(
            dataset_path,
            path
        )
        ct_wrangler = Wrangler(
            csv_path=csv_path,
            json_path=os.path.join(
                db_path,
                f'{ct}.json'
            )
        )
        logger.info(f'saving {ct} data as json')
        ct_wrangler.save_json()

    pass
