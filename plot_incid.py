#!/usr/bin/env python3

import pandas as pd
import plotly.express as px

if __name__ == '__main__':
    df = pd.read_csv("data/19a91d64-3cd3-42fc-9943-d635491a4d76", sep=";")
    df = df[df.cl_age90 == 0]
    france_met = df[df.dep.str.len() <= 2].groupby("jour", as_index=False).sum()
    france_met["dep"] = "fr_met"
    df2 = pd.concat((france_met, df[df.dep.isin(("01","69"))]), sort=False)
    df2["incid"] = df2.P / df2["pop"] * 100000
    plot = px.line(df2, x="jour", y="incid", color="dep", facet_row="dep",
            labels = {"jour":"Date", "incid":"Taux d'incidence / 100 000",
                "dep":"Département"})
    plot.update_layout(title="Taux d'incidence du Covid-19")
    plot.update_yaxes(matches=None)
    plot.write_html("/home/joel/public_html/covid_inc.html")
