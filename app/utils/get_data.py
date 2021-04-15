import pandas as pd
from urllib import request
from os import getcwd, path
import datetime
from helpers import ensure_dirs


COUNTIES_DATASET = 'https://github.com/nytimes/covid-19-data/raw/master/us-counties.csv'
STATES_DATASET = 'https://github.com/nytimes/covid-19-data/raw/master/us-states.csv'


def scrape_united_states_of_america():
    cwd = getcwd()
    us_dir = path.join(cwd, 'data', 'united_states_of_america')
    tmp_dir = path.join(cwd, 'tmp')

    ensure_dirs(us_dir, tmp_dir)

    headers = ['date', 'state', 'county',
               'place_type', 'fips', 'cases', 'deaths']

    counties_df = pd.read_csv(COUNTIES_DATASET)
    counties_df = counties_df.sort_values(
        by=['state', 'county', 'date'], ascending=[True, True, False])
    counties_df['place_type'] = 'county'
    counties_df = counties_df[headers]

    states_df = pd.read_csv(STATES_DATASET)
    states_df = states_df.sort_values(
        by=['state', 'date'], ascending=[True, False])
    states_df['county'] = ''
    states_df['place_type'] = 'state'
    states_df = states_df[headers]

    states_fips = {}
    fipses = states_df['fips'].unique()
    for fips in fipses:
        is_current_fips = states_df['fips'] == fips
        fips_file = path.join(us_dir, f'{fips:02d}.csv')
        current_df = states_df[is_current_fips]
        current_df.to_csv(fips_file, index=False, float_format='%.f')

        state = current_df['state'].iloc[0]
        is_same_fips = counties_df['state'] == state
        current_counties_df = counties_df[is_same_fips]
        current_counties_df.to_csv(
            fips_file, index=False, header=False, mode='a', float_format='%.f')

        states_fips[f'{fips:02d}'] = state

    with open(path.join(us_dir, 'README.md'), 'w') as readme_f:
        readme_f.write(get_readme_contents(states_fips))


def get_readme_contents(states):
    toc = [
        f'| {state} | [`{fips}.csv`]({fips}.csv) |' for fips, state in states.items()]
    toc_contents = '\n'.join(toc)
    return f"""## United States of America
> Last updated at {datetime.datetime.now(datetime.timezone.utc).strftime('%b %d %Y %H:%M:%S UTC')}.
| State | Dataset |
| ------ | ------- |
{toc_contents}
"""
