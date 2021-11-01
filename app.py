import sys, os
import pandas as pd
from flask import Flask, request

import jsonschema
from jsonschema import validate

sys.path.append("./libs") #In order to be able to solve relative path problems

from libs.predict import predict_and_save
from libs.train_model import load_train_save


valide_json_schema = {
    "type": "object",
    "properties": {
        "ph": {"type": "array"},
        "Hardness": {"type": "array"},
        "Solids": {"type": "array"},
        "Chloramines": {"type": "array"},
        "Sulfate": {"type": "array"},
        "Conductivity": {"type": "array"},
        "Organic_carbon": {"type": "array"},
        "Trihalomethanes": {"type": "array"},
        "Turbidity": {"type": "array"},
    },
    "additionalProperties": False
}
def validateJson(jsonData):
    try:
        validate(instance=jsonData, schema=valide_json_schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True


app = Flask(__name__)

@app.route('/predict', methods = ["GET"])
def entry_point():
    data = dict(request.json)
    print(data)
    if validateJson(data):
        df = pd.DataFrame(data)
        pred = predict_and_save(df)
        return str(pred)
    else:
        return "Enter a valid format please"

if __name__ == '__main__':
    app.run(debug=True, port=5000)