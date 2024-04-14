import pandas as pd
pd.plotting.register_matplotlib_converters()

def load(path: str) -> pd.DataFrame:
    """
    Load a csv file into a DataFrame
    write the dimensions of the DataFrame to the console
    return the DataFrame
    """
    # verify the path is not empty
    # if not path:
    #     print("path must not be an empty string")
    #     return None
    # # verify the path ends with '.csv'
    # elif not path.endswith('.csv'):
    #     print("path must end with '.csv'")
    #     return None
    # # verify the path exists
    # try:
    #     with open(path, 'r'):
    #         pass
    # except FileNotFoundError:
    #     print("path does not exist")
    #     return None
    # # load the csv file into a DataFrame
    # else:
    #     df = pd.read_csv(path)
    #     # write the dimensions of the DataFrame to the console
    #     print(f"Loading dataset of dimensions {df.shape}")
    #     # return the DataFrame
    #     return df
    try:
        if not os.path.exists(path):
            raise AssertionError("The file doesnt exist")
        if not path.lower().endswith('.csv'):
            raise AssertionError("The file fromat is not .csv")
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        exit()