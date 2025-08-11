import pandas as pd

class DataCleaner:
  def __init__(self, df: pd.DataFrame):
    self.df = df
    
  def fill_missing(self, column:str, strategy: str = "mean"):
    if strategy == "mean":
      self.df[column] = self.df[column].fillna(self.df[column].mean())
      
    elif strategy == "median":
      self.df[column] = self.df[column].fillna(self.df[column].median())
      
    elif strategy == "mode":
      self.df[column] = self.df[column].fillna(self.df[column].mode()[0])
      
    elif strategy == "null":
      self.df[column] = self.df[column].fillna(0)
    
    return self
      
  def drop_duplicates(self):
    self.df = self.df.drop_duplicates()
    return self
  
  def encode_columns(self,column:str, method:str):
    if method == "label":
      self.df[column] = self.df[column].astype("category").cat.codes
    return self
  
  def preview(self, rows:int=5):
    return self.df.head(rows)

  def get_df(self):
    return self.df      