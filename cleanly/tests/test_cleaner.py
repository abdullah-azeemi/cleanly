import pandas as pd
from cleanly.core import DataCleaner

def test_fill_missing():
  df = pd.DataFrame({"A": [1,None,3]})
  cleaner = DataCleaner(df).fill_missing("A","mean")
  assert cleaner.get_df()["A"].isnull().sum() == 0
  