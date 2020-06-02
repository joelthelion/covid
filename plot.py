#!/usr/bin/env python3

import pandas as pd
import plotly.express as px

if __name__ == '__main__':
    df = pd.read_csv("data/6fadff46-9efd-4c53-942a-54aca783c30c", sep=";")
    france_met = df[df.dep.str.len() <= 2].groupby("jour", as_index=False).sum()
    france_met["dep"] = "France"
    df2 = pd.concat((france_met, df[df.dep.isin(("01","69"))]))
    print(df2)
    plot = px.line(df2, x="jour", y="incid_hosp", color="dep", facet_row="dep",
            labels = {"jour":"Date", "incid_hosp":"Nouvelles hospitalisations",
                "dep":"Département"})
    plot.update_layout(title="Nouvelles hospitalisations dues au Covid-19")
    plot.update_yaxes(matches=None)
    plot.show()
