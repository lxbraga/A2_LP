from data_processing.Database_Connection_Classes import ConnFifa as dff
from data_processing.Database_Connection_Classes import ConnCovid as dfc
import pandas as pd

class CleanFifa:
    def __init__(self):
        '''
        init da classe CleanFifa

        Returns
        -------
        None.

        '''
        self.df = dff().df_creator()

    def drop_cols(self, df):
        '''
        Essa função limpa as colunas do dataset Fifa.

        Parameters
        ----------
        df : set
            Dataset Fifa.

        Returns
        -------
        df : set
            Dataset Fifa.

        '''
        df = df.drop(["Photo","Flag","Club_Logo", "Loaned_From", "Release_Clause", "Joined"],axis=1)
        df = df[df["Weight"].notna()]
        df = df.dropna()    
        return df

    def convert_to_float(self, df):
        '''
        Conversão dos dados para float.

        Parameters
        ----------
        df : set
            Dataset Fifa.

        Returns
        -------
        value : float
            Retorna os valores convertidos em float.

        '''
        try:
            value = float(df[1:-1])

            if df[-1:] == "M":
                value = value * 1000000
            elif df[-1:] == "K":
                value = value * 1000
        except ValueError:
            value = 0
        return value

    def convert_lbs_kg(self, value):
        '''
        Essa função converte libras para quilogramas.

        Parameters
        ----------
        value : float
            Valor a ser convertido.

        Raises
        ------
        ValueError
            Valor não corresponde a unidade libras.

        Returns
        -------
        value : float
            Valor correspondente de Libras para Quilogramas.

        '''
        if value[-3:] != "lbs":
            raise ValueError
        value = round(float(value[:-3]) * 0.45359237, 0)
        return value

    def convert_ft_meters(self, value):
        '''
        Essa função converte pés para metros.

        Parameters
        ----------
        value : float
            Valor a ser convertido.

        Raises
        ------
        ValueError
            Esse valor não corresponde a unidade pés.

        Returns
        -------
        ft : float
            Valor final convertido.

        '''
        if value[1] != "\'":
            raise ValueError
        ft = round(((int(value[0]) * 12) + int(value[2:])) * 0.0254, 2)
        return ft
            
    def remove_plus(self, value):
        '''
        Essa função remove os "+".

        Parameters
        ----------
        value : int
            Valor que vai ser convertido.

        Raises
        ------
        ValueError
            Esse valor não tem um "+" para ser retirado.

        Returns
        -------
        value : int
            valor final convertido.

        '''
        if value[-2] != "+":
            raise ValueError
        value = int(value[:-2])
        return value

    def apply_convert(self, df):
        '''
        Essa função converte os datasets para as novas unidades de medida.

        Parameters
        ----------
        df : set
            Data set que vai ser convertido de acordo com as mudanças anteriores.

        Returns
        -------
        df : set
            Dataset finalmente convertido e modificado.

        '''
        ind = df.columns.get_loc("LS")
        with_plus = df.columns[ind:ind+26]
        for i in with_plus:
            df[i] = df[i].apply(self.remove_plus)
        df["Value"], df["Wage"] = df["Value"].apply(self.convert_to_float), df["Wage"].apply(self.convert_to_float)
        df["Weight"] = df["Weight"].apply(self.convert_lbs_kg)
        df["Height"] = df["Height"].apply(self.convert_ft_meters)
        return df

    def fetcher(self):
        '''
        Esse função é o fetcher

        Returns
        -------
        set
            Dataset to csv.

        '''
        self.df = self.drop_cols(self.df)
        self.df = self.apply_convert(self.df)
        self.df.to_csv(f"CSVs/fifa_limpo.csv", index = False)
        return self.df


class CleanCovid:
    def __init__(self):
        '''
        Init da class CleanCovid

        Returns
        -------
        None.

        '''
        self.df = dfc().df_creator()
    
    def drop_cols(self, df):
        '''
        Essa função limpa as colunas do dataset Covid.

        Parameters
        ----------
        df : set
            Dataset ovid.

        Returns
        -------
        df : set
            Dataset ovid com colunas retiradas.

        '''
        df = df.drop(["AggregationMethod", "Version"],axis=1)    
        return df
        
    def convert(self, df):
        '''
        Converte o Dataset Covid

        Parameters
        ----------
        df : set
            Dataset para conversão.

        Returns
        -------
        df : set
            Dataset convertido.

        '''
        df["Date"] = pd.to_datetime(df["Date"])
        return df
    
    def fetcher(self):
        '''
        Esse função é o fetcher

        Returns
        -------
        set
            Dataset to csv.

        '''
        self.df = self.drop_cols(self.df)
        self.df = self.convert(self.df)
        self.df.to_csv(f"CSVs/covid_limpo.csv", index = False)
        return self.df
