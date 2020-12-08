import pyodbc
import pandas as pd

class Connection:
        
    def __init__(self):
        '''
        Função init da classe Connection

        Returns
        -------
        None.

        '''
        self.tablenames = ["covid.covid_impact_on_airport_traffic",
                           "fifa.fifa_players",
                           "real_state.real_state_values",
                           "ufc.ufc_master",
                           "ufc.ufc_most_recent_event",
                           "ufc.ufc_upcoming_event"]
        self.server = "fgv-db-server.database.windows.net" 
        self.db = "fgv-db"
        self.user = "student" 
        with open("PWD") as f: #Arquivo com a senha para passar implicitamente
            self.pwd = f.read()
        self.driver = "{ODBC Driver 17 for SQL Server}"
        
    def connection(self):
        '''
        Função que fornece as informações necessárias para que haja
        a conexão com o banco de dados

        Returns
        -------
        pipe
            Retorna a conexão com o banco de dados.

        '''
        self.conn = pyodbc.connect(f"DRIVER={self.driver};\
                          SERVER={self.server};\
                          DATABASE={self.db};\
                          UID={self.user};\
                          PWD={self.pwd};\
                          PORT=1433;")
        return self.conn
    
    def df_creator(self, table):
        '''
        Cria do dataframe de acordo com a tabela escolhida.

        Parameters
        ----------
        table : string
            Nome dado as tabelas.

        Raises
        ------
        ValueError
            O selecionado não está compreendido dentre os disponíveis.

        Returns
        -------
        df : set
            Dataframe lida .

        '''
        if table not in self.tablenames:
            raise ValueError(f"Por favor, escolha uma das seguintes tabelas:\n {self.tablenames}")
        query = f"SELECT * FROM {table}"
        df = pd.read_sql(query, self.connection())
        df.to_csv(f"CSVs/{table.split('.')[0]}_sujo.csv", index = False)
        return df
        
class ConnFifa(Connection):
    def __init__(self):
        '''
        Função init da classe ConnFifa

        Returns
        -------
        None.

        '''
        super().__init__()
    def connection(self):
        '''
        Função que fornece as informações necessárias para que haja
        a conexão com o banco de dados

        Returns
        -------
        pipe
            Retorna a conexão com o banco de dados.

        '''
        super().connection()
    def df_creator(self):
        '''
        Cria do dataframe de acordo com a tabela escolhida.

        Parameters
        ----------
        table : string
            Nome dado as tabelas.

        Raises
        ------
        ValueError
            O selecionado não está compreendido dentre os disponíveis.

        Returns
        -------
        df : set
            Dataframe lida .

        '''
        table = "fifa.fifa_players"
        return Connection().df_creator(table)        
        

class ConnCovid(Connection):
    def __init__(self):
        '''
        Função init da classe ConnCovid

        Returns
        -------
        None.

        '''
        super().__init__()
    def connection(self):
        '''
        Função que fornece as informações necessárias para que haja
        a conexão com o banco de dados

        Returns
        -------
        pipe
            Retorna a conexão com o banco de dados.

        '''
        super().connection()
    def df_creator(self):
        '''
        Cria do dataframe de acordo com a tabela escolhida.

        Parameters
        ----------
        table : string
            Nome dado as tabelas.

        Raises
        ------
        ValueError
            O selecionado não está compreendido dentre os disponíveis.

        Returns
        -------
        df : set
            Dataframe lida .

        '''
        table = "covid.covid_impact_on_airport_traffic"
        return Connection().df_creator(table)   
