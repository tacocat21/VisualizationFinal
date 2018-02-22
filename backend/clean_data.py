import pandas as pd
import ipdb
import collections
import util
from util import save_json

CONTINENT = set(['AFRICA', 'LATIN AMERICA AND THE CARIBBEAN', 'NORTHERN AMERICA', 'EUROPE', 'ASIA', 'OCEANIA'])
REGIONS = set(['Eastern Africa', 'Middle Africa', 'Northern Africa', 'Southern Africa',
               'Western Africa', 'Central Asia', 'Eastern Asia', 'Southern Asia',
               'South-Eastern Asia', 'Western Asia', 'Eastern Europe', 'Northern Europe',
               'Southern Europe', 'Western Europe', 'Caribbean', 'Central America',
               'South America', 'Australia/New Zealand', 'Melanesia', 'Micronesia',
               'Polynesia', 'North America'])
IGNORE = set(['Sub-Saharan Africa',
              'More developed regions',
              'Less developed regions',
              'Least developed countries',
              'Less developed regions, excluding least developed countries',
              'High-income countries',
              'Middle-income countries',
              'Upper-middle-income countries',
              'Lower-middle-income countries',
              'Low-income countries', 'WORLD'])


def load_data():
    return pd.read_excel(util.UN_ORIGINAL_DATA_FILENAME, skiprows=15, sheet_name='Table 1', convert_float=True)


def get_year(row):
    try:
        return int(row[0])
    except ValueError:
        return None


def get_location(row):
    return row[2]


def get_top_n(row, n=10):
    # countries = row.keys()[9:]
    if type(row) is pd.core.series.Series:
        return row[9:].replace(to_replace='..', value=-1).sort_values(ascending=False).head(n).to_dict()
    elif type(row) is collections.defaultdict:
        # ipdb.set_trace()
        return dict(sorted(row.items(), key=lambda x:x[1], reverse=True)[:n])

def country_to_region_mapping(df):
    process = df[12:270]
    country_region_mapping = collections.defaultdict(str)
    region = None
    for _, row in process.iterrows():
        location = get_location(row)
        if location in CONTINENT:
            continue
        if region is None or location in REGIONS:
            region = location
            continue
        assert region in REGIONS
        country_region_mapping[location] = region
    return country_region_mapping

def run():
    df = load_data()
    country_region_mapping = country_to_region_mapping(df)
    # ipdb.set_trace()
    # year -> region ->
    # immigration result -> going to [year][country]
    # emigration result -> leaving [year][country]
    immigration_region_result = collections.defaultdict(lambda: collections.defaultdict(dict))
    emigration_region_result = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(int)))
    # year -> country -> top 10 countries immigrating/emigrating to country
    immigration_country_result = collections.defaultdict(lambda: collections.defaultdict(dict))
    emigration_country_result = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(int)))
    for _, row in df.iterrows():
        year = get_year(row)
        if year is None:
            continue
        location = get_location(row)
        if location in IGNORE or location in CONTINENT:
            continue
        elif location in REGIONS:
            # ipdb.set_trace()
            region_sum = collections.defaultdict(int)
            for c in row.keys()[9:]:
                try:
                    region_sum[country_region_mapping[c]] += int(row[c])
                except ValueError:
                    continue
            top_10 = get_top_n(region_sum, n=10)
            immigration_region_result[year][location] = top_10
        else:
            top_10 = get_top_n(row, n=10)
            immigration_country_result[year][location] = top_10
            # ipdb.set_trace()
            for c in row.keys()[9:]:
                try:
                    emigration_country_result[year][c][location] = int(row[c])
                except ValueError:
                    continue
    # ipdb.set_trace()
    for y in emigration_country_result:
        for c in emigration_country_result[y]:
            region = country_region_mapping[c]
            for k in emigration_country_result[y][c]:
                emigration_region_result[y][region][country_region_mapping[k]] += emigration_country_result[y][c][k]
    for y in emigration_region_result:
        for c in emigration_region_result[y]:
            emigration_region_result[y][c] = get_top_n(emigration_region_result[y][c])
    for y in emigration_country_result:
        for c in emigration_country_result[y]:
            # for l in emigration_country_result[y][c]:
            emigration_country_result[y][c] = get_top_n(emigration_country_result[y][c], n=10)
    # ipdb.set_trace()
    save_json(emigration_region_result, util.EMIGRATION_REGION_DATA_FILENAME)
    save_json(emigration_country_result, util.EMIGRATION_COUNTRY_DATA_FILENAME)
    save_json(immigration_region_result, util.IMMIGRATION_REGION_DATA_FILENAME)
    save_json(immigration_country_result, util.IMMIGRATION_COUNTRY_DATA_FILENAME)



if __name__ == "__main__":
    # df = load_data()
    run()
    ipdb.set_trace()
    # print(df)
