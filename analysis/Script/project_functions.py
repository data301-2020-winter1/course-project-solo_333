#!/usr/bin/env python
# coding=utf-8
import pandas as pd
import pandas as pd
import numpy as np
from sklearn.datasets import load_wine

def load_and_process(url_or_path_to_csv_file):
    df=pd.read_csv(url_or_path_to_csv_file, encoding= 'unicode_escape')

    df.dropna()
    df = (
        df
        .assign(Weekend=lambda x: x["Weekend?"]=="Weekend")
        .assign(DateTime=lambda x:pd.to_datetime(x["Year"] + x["Month"] + x["Hour"]))
        .rename(columns={"Injury Type":"Type"})
        .dropna()
        .drop(['Weekend?',"Year","Month","Hour"],axis=1)
        .sort_values("Master Record Number", ascending=True)
        .reset_index()
    )
    df.to_csv("./processed/monroe-county-crash-data2003-to-2015.csv")
    
    return df
