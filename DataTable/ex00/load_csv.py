import pandas as pd
pd.plotting.register_matplotlib_converters()


def load(path: str) -> pd.DataFrame:
    """
    Load a csv file into a DataFrame
    write the dimensions of the DataFrame to the console
    return the DataFrame
    """
    try:
        with open(path, 'r'):
            df = pd.read_csv(path)
            print(f"Loading dataset of dimensions {df.shape}")
            return df

    except FileNotFoundError:
        print("path does not exist or could not be opened")
        return None
