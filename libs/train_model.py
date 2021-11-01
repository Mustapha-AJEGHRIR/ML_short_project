# ------------------------------ Primitive libs ------------------------------ #
import os
from joblib import dump, load
import numpy as np
from datetime import datetime

# -------------------------------- Local libs -------------------------------- #
from process_old_new import process_old_new
from configurations import training_columns, predict_column, Square

def relative_path(path):
    dirname = os.path.dirname(__file__)
    return os.path.join(dirname, path)


def load_train_save(path="../model/final_model.joblib", backup=True, backup_path = "../model/backup/"):
    # ------------------------ lets get rid of relativity ------------------------ #
    path = relative_path(path)
    backup_path = relative_path(backup_path+datetime.now().strftime("%d-%m-%Y_%H-%M-%S")+".joblib")
    # ----------------------------------- Load ----------------------------------- #
    final_model = load(path)
    # ---------------------------------- Backup ---------------------------------- #
    dump(final_model, backup_path)
    # ----------------------------------- Train ---------------------------------- #
    data = process_old_new()
    X, y = data[training_columns].to_numpy(), data[predict_column].to_numpy()
    final_model.fit(X, np.ravel(y))
    # ----------------------------------- Save ----------------------------------- #
    dump(final_model, path)

if __name__=="__main__":
    load_train_save()



