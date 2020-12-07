# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 00:51:50 2020

@author: Lucas Braga
"""

import pyodbc
import pandas as pd


tablenames = ["covid.covid_impact_on_airport_traffic",
              "fifa.fifa_players",
              "real_state.real_state_values",
              "ufc.ufc_master",
              "ufc.ufc_most_recent_event",
              "ufc.ufc_upcoming_event"]
server = "fgv-db-server.database.windows.net" 
db = "fgv-db"
user = "student" 
pwd = "@dsInf123"
driver = "{ODBC Driver 17 for SQL Server}"

def connection():
    conn = pyodbc.connect(f"DRIVER={driver};\
                      SERVER={server};\
                      DATABASE={db};\
                      UID={user};\
                      PWD={pwd};\
                      PORT=1433;")
    return conn

def df_creator(table):
    if table not in tablenames:
        raise ValueError(f"Por favor, escolha uma das seguintes tabelas:\n {tablenames}")
    query = f"SELECT * FROM {table}"
    df = pd.read_sql(query, connection())
    return df

df = df_creator("fifa.fifa_players")
print(df.describe().T)

print(pyodbc.drivers())