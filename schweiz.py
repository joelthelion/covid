#!/usr/bin/env python3

import requests
import pandas as pd


def get_schweiz():
    """ Return schweizer covid data """
    context = requests.get("https://www.covid19.admin.ch/api/data/context").json()
    cases = context["sources"]["individual"]["csv"]["daily"]["cases"]
    df = pd.read_csv(cases)
    return df


def to_fr(df):
    """ Convert to french format """
    return df[["datum", "geoRegion", "inz_entries"]]\
            .rename(columns={"datum": "jour", "geoRegion": "dep", "inz_entries": "incid"})


if __name__ == '__main__':
    get_schweiz()
