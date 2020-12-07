# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 03:12:52 2020

@author: Lucas Braga
"""
from Database_Connection import df_creator as dfc
table = "fifa.fifa_players"
df = dfc(table)

def drop_cols(df):
    #if tablename == "fifa":
    df = df.drop(["Photo","Flag","Club_Logo", "Loaned_From", "Release_Clause", "Joined"],axis=1)
    df = df[df["Weight"].notna()]
    df = df.dropna()    
    return df

def convert_to_float(df):
    try:
        value = float(df[1:-1])

        if df[-1:] == "M":
            value = value * 1000000
        elif df[-1:] == "K":
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
        
def remove_plus(value):
    if value[-2] != "+":
        raise ValueError
    value = int(value[:-2])
    return value

def apply_convert(df):
    ind = df.columns.get_loc("LS")
    with_plus = df.columns[ind:ind+26]
    for i in with_plus:
        df[i] = df[i].apply(remove_plus)
    df["Value"], df["Wage"] = df["Value"].apply(convert_to_float), df["Wage"].apply(convert_to_float)
    df["Weight"] = df["Weight"].apply(convert_lbs_kg)
    df["Height"] = df["Height"].apply(convert_ft_meters)
    return df

def fetcher(df):
    df = drop_cols(df)
    df = apply_convert(df)
    df.to_csv(f"CSVs/{table.split('.')[0]}_limpo.csv")
    return df

df = fetcher(df)
#df = apply_convert(drop_cols(df))
