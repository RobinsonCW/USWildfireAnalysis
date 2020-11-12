import json
import os

from categorizer_lambda.ml_utils import get_model, predict_from_event
from categorizer_lambda.db_utils import get_secret, insert_prediction

MODEL_BUCKET = os.environ.get("MODEL_BUCKET")
PIPELINE_PATH = os.environ.get("MODEL_PIPELINE_PATH")
CLASSIFIER_PATH = os.environ.get("MODEL_CLASSIFIER_PATH")

MODEL = get_model(MODEL_BUCKET, (PIPELINE_PATH, CLASSIFIER_PATH))


def lambda_handler(event, context):
    result = predict_from_event(event, model=MODEL)
    params = get_secret()
    primary_key = insert_prediction(params, result)
    result["db_primary_key"] = primary_key
    return {"body": json.dumps(result), "statusCode": 200}
