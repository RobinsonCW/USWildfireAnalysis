from collections import namedtuple
from io import BytesIO
from typing import Tuple

import boto3
import numpy as np
import joblib

MyModel = namedtuple("MyModel", ["vectorizer", "classifier"])


def get_model(bucket: str, object_keys: Tuple[str, str]) -> MyModel:
    s3 = boto3.resource("s3").Bucket(bucket)
    # # with BytesIO() as vec:
    # #     s3.download_fileobj(Key=object_keys[0], Fileobj=vec)
    # #     vectorizer = joblib.load(vec)

    with BytesIO() as clas:
        s3.download_fileobj(Key=object_keys[1], Fileobj=clas)
        classifier = joblib.load(clas)

    # classifier = joblib.load(
    #     "/Users/robinsoncw/github/smu/USWildfireAnalysis/src/exploratory_data_analysis/chance/python/aws_predict/training/models/decission_tree_classifier.pkl"
    # )

    return MyModel(classifier, classifier)


def predict_from_event(event, model: MyModel) -> list:
    data = event["body"]
    return predict(data, model)


def predict(data: str, model: MyModel) -> list:
    data = data.strip("][").split(", ")
    # Convert strings inside list to float
    data_list_of_floats = list(map(float, data))

    data2 = [data_list_of_floats]

    print(f"Classifying {data2}")

    pred_label = model.classifier.predict(data2)
    pred_proba = model.classifier.predict_proba(data2)
    max_proba = np.argmax(pred_proba, axis=1)
    proba_perc = pred_proba[[0][0]][int(max_proba)]

    answer = {}
    answer["prediction_label"] = pred_label[0]
    answer["prediction_probability"] = "{:.4f}".format(proba_perc)
    answer["payload"] = data

    return answer
