import pandas as pd
import os

def get_data(data_dir: str, filename: str) -> pd.DataFrame:
    path: str = os.path.join(data_dir, filename)
    return pd.read_csv(path)['tokenized_text']