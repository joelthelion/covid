#!/usr/bin/env python3

import pandas as pd
import plotly.express as px

if __name__ == '__main__':
    df = pd.read_csv("data/6fadff46-9efd-4c53-942a-54aca783c30c", sep=";")
    print(df)
    print(df)
    plot = px.line(df, x="jour", y="incid_hosp", color="dep")
    plot.show()
