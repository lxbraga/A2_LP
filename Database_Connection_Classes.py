import pyodbc
import pandas as pd

class Connection():
        
    def __init__(self):
        self.tablenames = ["covid.covid_impact_on_airport_traffic",
                           "fifa.fifa_players",
                           "real_state.real_state_values",
                           "ufc.ufc_master",
                           "ufc.ufc_most_recent_event",
                           "ufc.ufc_upcoming_event"]
        self.server = "fgv-db-server.database.windows.net" 
        self.db = "fgv-db"
        self.user = "student" 
        self.pwd = "@dsInf123"
        self.driver = "{ODBC Driver 17 for SQL Server}"
        
    def connection(self):
        self.conn = pyodbc.connect(f"DRIVER={self.driver};\
                          SERVER={self.server};\
                          DATABASE={self.db};\
                          UID={self.user};\
                          PWD={self.pwd};\
                          PORT=1433;")
        return self.conn
    
    def df_creator(self, table):
        self.table = table
        if table not in self.tablenames:
            raise ValueError(f"Por favor, escolha uma das seguintes tabelas:\n {self.tablenames}")
        query = f"SELECT * FROM {self.table}"
        df = pd.read_sql(query, self.connection())
        #df.to_csv(f"CSVs/{table.split('.')[0]}_sujo.csv")
        return df

class ConnFifa(Connection):
    def __init__(self):
        super().__init__()
    def connection(self):
        super().connection()
    def df_creator(self, table = "fifa.fifa_players"):
        df = Connection().df_creator(table)
        return df
        
        

class ConnCovid(Connection):
    def __init__(self):
        super(self).__init__(self)
    def connection(self):
        super(self).connection()
    def df_creator(self, table = "covid.covid_impact_on_airport_traffic"):
        super(self).df_creator(self)

df = ConnFifa().df_creator()
#print(df.describe().T)

#print(pyodbc.drivers())