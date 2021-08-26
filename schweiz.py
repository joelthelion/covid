#!/usr/bin/env python3

import requests
import pandas as pd


def get_schweiz():
    """ Return schweizer covid data """
    context = requests.get("https://www.covid19.admin.ch/api/data/context").json()
    print(context)
    cases = context["sources"]["individual"]["csv"]["daily"]["cases"]
    print(cases)
    df = pd.read_csv(cases)
    print(df)
    print(df.columns)
    return df


def to_fr(df):
    """ Convert to french format """
    return df[["datum", "geoRegion", "inz_entries"]]\
            .rename(columns={"datum": "jour", "geoRegion": "dep", "inz_entries": "incid"})


if __name__ == '__main__':
    get_schweiz()
