from data_processing.Database_Connection_Classes import ConnFifa as dff
from data_processing.Database_Connection_Classes import ConnCovid as dfc

class CleanFifa:
    def __init__(self):
        self.df = dff().df_creator()

    def drop_cols(self, df):
        df = df.drop(["Photo","Flag","Club_Logo", "Loaned_From", "Release_Clause", "Joined"],axis=1)
        df = df[df["Weight"].notna()]
        df = df.dropna()    
        return df

    def convert_to_float(self, df):
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
        if value[-3:] != "lbs":
            raise ValueError
        value = round(float(value[:-3]) * 0.45359237, 0)
        return value

    def convert_ft_meters(self, value):
        if value[1] != "\'":
            raise ValueError
        ft = round(((int(value[0]) * 12) + int(value[2:])) * 0.0254, 2)
        return ft
            
    def remove_plus(self, value):
        if value[-2] != "+":
            raise ValueError
        value = int(value[:-2])
        return value

    def apply_convert(self, df):
        ind = df.columns.get_loc("LS")
        with_plus = df.columns[ind:ind+26]
        for i in with_plus:
            df[i] = df[i].apply(self.remove_plus)
        df["Value"], df["Wage"] = df["Value"].apply(self.convert_to_float), df["Wage"].apply(self.convert_to_float)
        df["Weight"] = df["Weight"].apply(self.convert_lbs_kg)
        df["Height"] = df["Height"].apply(self.convert_ft_meters)
        return df

    def fetcher(self):
        self.df = self.drop_cols(self.df)
        self.df = self.apply_convert(self.df)
        df.to_csv(f"CSVs/{table.split('.')[0]}_limpo.csv", index = False)
        return self.df


class CleanCovid:
    def __init__(self):
        self.df = dfc().df_creator()
    
    def drop_cols(self, df):
        df = df.drop(["AggregationMethod", "Version"],axis=1)    
        return df
        
    def convert(self, df)
        df["Date"] = pd.to_datetime(covid["Date"])
        return df
    
    def fetcher(self):
        self.df = self.drop_cols(self.df)
        self.df = self.convert(self.df)
        df.to_csv(f"CSVs/{table.split('.')[0]}_limpo.csv", index = False)
        return self.df
