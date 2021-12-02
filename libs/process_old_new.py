import os
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

from configurations import limits

def relative_path(path):
    dirname = os.path.dirname(__file__)
    return os.path.join(dirname, path)

def row_indexer(dataset, limits):
    """
    This function will return the indexes of row that are labeled as potable but should not be potable (out of the limits)
    """
    index = np.zeros(len(dataset))
    for key,(minimum, maximum) in limits.items():
        index = index | ( (dataset[key] < minimum) | (dataset[key] > maximum) ) & dataset["Potability"]
    return index


def data_processing(data, limits, weights_init=1, weights_modif=0.5):

    data = pd.DataFrame(SimpleImputer().fit_transform(data), columns=data.columns)

    weights = pd.DataFrame(np.ones(len(data))*weights_init, columns=["Weights"])
    data.insert(0, "Weights", weights)

    indexes = row_indexer(data, limits)
    data.loc[ indexes, "Weights"] = weights_modif
    data.loc[ indexes, "Potability"] = 0

    return data

def process_old_new(old_path="../data/drinking_water_potability.csv", 
        new_path="../new_data/raw_data.csv",
        out_path="../inputs/processed_data.csv",
        limits=limits,
        weights_init = 1,
        weights_modif = 0.5) -> pd.DataFrame():
    """This function will concatenate 2 datasets then do preprocessing on them
    The preprocessing starts by a simple Imputer then relabilization of datapoints, relabeling potable water out 
    of the permissible limits as non potable

    Args:
        old_path (str, optional): Path to the old file. Defaults to "../data/drinking_water_potability.csv", 
        new_path="../new_data/raw_data.csv", 
        limits={  "ph" : (6.5, 8.5), "Trihalomethanes" : (0, 80), "Turbidity" : (0,5)}, 
        weights_init = 1, 
        weights_modif = 0.5)->pd.DataFrame(.

    Returns:
        pd.DataFrame: a preprocessed dataFrame
    """
    # --------- Lets first have no more problems with relativity of paths -------- #
    old_path = relative_path(old_path)
    new_path = relative_path(new_path)
    out_path = relative_path(out_path)
    # -------------------------------- Start here -------------------------------- #
    old_data = pd.read_csv(old_path,index_col= False)
    new_data = pd.read_csv(new_path,index_col= False)
    concat = pd.concat((old_data, new_data))
    # ---------------------------------- Process --------------------------------- #
    processed_data = data_processing(concat, limits, weights_init, weights_modif)
    processed_data.to_csv(out_path, index = False)
    return processed_data

if __name__ == "__main__":
    process_old_new()
    


