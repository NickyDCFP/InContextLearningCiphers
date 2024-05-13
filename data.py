import pandas as pd
import os

def get_data(data_dir: str, filename: str) -> pd.DataFrame:
    """
    Gets the dataset from the data directory with the particular filename

    Parameters:
        data_dir:   The directory containing the dataset csv.
        filename:   The filename for the dataset.
    
    Returns:
        The dataset as a singular column of a DataFrame.
    """
    path: str = os.path.join(data_dir, filename)
    return pd.read_csv(path)['tokenized_text']