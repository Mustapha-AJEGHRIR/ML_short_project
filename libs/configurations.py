import numpy as np

# ---------------------------------- Sklearn --------------------------------- #
from sklearn.base import BaseEstimator, TransformerMixin

class Square(BaseEstimator, TransformerMixin):
  def __init__(self):
    pass
  def fit(self, X, y=None):
    return self
  def transform(self, X, y=None):
    return np.concatenate((X, X**2), axis=1)


# ---------------- Used features for Training and predictions ---------------- #
training_columns = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity','Organic_carbon', 'Trihalomethanes', 'Turbidity']
predict_column = ['Potability']

# ---------------------- Limits used to preprocess data ---------------------- #
limits = { #Containnig (min, max) for potability
    "ph" : (6.5, 8.5), #WHO Standard https://www.who.int/water_sanitation_health/dwq/chemicals/ph_revised_2007_clean_version.pdf
    # "Solids" : (50, 1000), #TDS Limits https://www.kent.co.in/blog/what-are-total-dissolved-solids-tds-how-to-reduce-them/
    "Trihalomethanes" : (0, 80), #EPA Standards https://www.epa.gov/sites/default/files/2016-06/documents/npwdr_complete_table.pdf
    "Turbidity" : (0,5) #WHO Standard https://www.lenntech.com/turbidity.htm#:~:text=The%20WHO%20(World%20Health%20Organization,ideally%20be%20below%201%20NTU.
}

