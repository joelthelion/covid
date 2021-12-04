#!/usr/bin/env python3

from datetime import datetime
import pandas as pd
import plotly.express as px
from schweiz import get_schweiz, to_fr


def load():
    """Load and merge various data sources"""
    df = pd.read_csv(
        "data/19a91d64-3cd3-42fc-9943-d635491a4d76", sep=";", dtype={"dep": "string"}
    )
    df = df[df.cl_age90 == 0]
    france_met = df[df.dep.str.len() <= 2].groupby("jour", as_index=False).sum()
    france_met["dep"] = "fr_met"
    df2 = pd.concat((france_met, df[df.dep.isin(("01", "69"))]), sort=False)
    df2["incid"] = df2.P / df2["pop"] * 100000
    df_ch = to_fr(get_schweiz())
    df_ch = df_ch[df_ch.dep.isin(["VD", "CH"])]
    df2 = pd.concat([df_ch, df2])
    return df2


def plot(df):
    """Plot incidence dataframe"""
    plot = px.line(
        df,
        x="jour",
        y="incid",
        color="dep",
        facet_col="dep",
        facet_col_wrap=1,
        labels={
            "jour": "Date",
            "incid": "Taux d'incidence / 100 000",
            "dep": "Département",
        },
    )
    plot.update_layout(title="Taux d'incidence du Covid-19")
    plot.update_xaxes(range=["2021-03-01", datetime.now()])
    plot.update_yaxes(range=[0, 200])
    plot.write_html("/home/joel/public_html/covid_inc.html")


if __name__ == "__main__":
    df = load()
    plot(df)
