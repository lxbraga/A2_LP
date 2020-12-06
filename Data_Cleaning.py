# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 03:12:52 2020

@author: Lucas Braga
"""

def drop_cols(df):
    #if tablename == "fifa":
    df = df.drop(["Photo","Flag","Club_Logo", "Loaned_From", "Release_Clause", "Joined"],axis=1)
    df = df[df["Weight"].notna()]
        
    return df

def convert_to_float(df):
    try:
        value = float(df[1:-1])
        suffix = df[-1:]

        if suffix == 'M':
            value = value * 1000000
        elif suffix == 'K':
            value = value * 1000
    except ValueError:
        value = 0
    return value

def apply_convert(df):
    cols = ["Value", "Wage"]
    for col in cols:
        df.loc[:, col] = df[col].apply(convert_to_float)
    return df


#df = apply_convert(drop_cols(df))
