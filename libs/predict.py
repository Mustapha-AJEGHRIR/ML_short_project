from joblib import dump, load
import os
from csv import writer
import numpy as np

from configurations import Square


def relative_path(path):
    dirname = os.path.dirname(__file__)
    return os.path.join(dirname, path)

def predict(X, model_path="../model/final_model.joblib"):
    # ------------------------- get rid of relative paths ------------------------ #
    model_path = relative_path(model_path)
    # -------------------------------- bring model ------------------------------- #
    final_model = load(model_path)
    # ----------------------------- Predict and proba ---------------------------- #
    pred = final_model.predict(X)
    pred_prob = final_model.predict_proba(X)
    return pred, pred_prob

def predict_and_save(X, threshold=0.9, model_path="../model/final_model.joblib", new_data_path="../new_data/raw_data.csv" ):
    pred, pred_prob = predict(X, model_path="../model/final_model.joblib")
    # ------------------------- get rid of relativs paths ------------------------ #
    new_data_path = relative_path(new_data_path)
    # --------------------------- Find good predictions -------------------------- #
    indexer = (pred_prob>threshold).sum(axis=1) == 1 #the ==1 is in order to have indexer a bool array
    data_to_save = np.concatenate((X[indexer], pred[indexer].reshape(-1,1)), axis=1)
    # --------------- Put them on the new_data file as ground truth -------------- #
    with open(new_data_path, 'a') as file_object:
        writer_object = writer(file_object, lineterminator='\n')
        writer_object.writerows(data_to_save)
    return pred
        

if __name__=="__main__":
    predict_and_save(np.array([[7,204.8904555,20791.31898,7.300211873,368.5164413,564.3086542,10.37978308,86.99097046,2.963135381],[1,204.8904555,20791.31898,7.300211873,368.5164413,564.3086542,10.37978308,86.99097046,2.963135381]]))