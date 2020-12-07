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

        if suffix == "M":
            value = value * 1000000
        elif suffix == "K":
            value = value * 1000
    except ValueError:
        value = 0
    return value

def convert_lbs_kg(value):
    if value[-3:] != "lbs":
        raise ValueError
    value = round(float(value[:-3]) * 0.45359237, 0)
    return value

def convert_ft_meters(value):
    if value[1] != "\'":
        raise ValueError
    ft = round(((int(value[0]) * 12) + int(value[2:])) * 0.0254, 2)
    return ft
        
    

def apply_convert(df):
    df["Values"], df["Wage"] = df["Value"].apply(convert_to_float), df["Wage"].apply(convert_to_float)
    df["Weight"] = df["Weight"].apply(convert_lbs_kg)
    df["Height"] = df["Height"].apply(convert_ft_meters)
    return df


#df = apply_convert(drop_cols(df))
