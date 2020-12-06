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

