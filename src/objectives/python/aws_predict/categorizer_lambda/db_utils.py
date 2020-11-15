import psycopg2
import boto3
import base64
from botocore.exceptions import ClientError


def get_secret():
    # Use this code snippet in your app.
    # If you need more information about configurations or implementing the sample code, visit the AWS docs:
    # https://aws.amazon.com/developers/getting-started/python/

    secret_name = "prod/aws_predict/postgres"
    region_name = "us-west-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region_name)

    # In this sample we only handle the specific exceptions for the 'GetSecretValue' API.
    # See https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    # We rethrow the exception by default.

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        if e.response["Error"]["Code"] == "DecryptionFailureException":
            # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response["Error"]["Code"] == "InternalServiceErrorException":
            # An error occurred on the server side.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response["Error"]["Code"] == "InvalidParameterException":
            # You provided an invalid value for a parameter.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response["Error"]["Code"] == "InvalidRequestException":
            # You provided a parameter value that is not valid for the current state of the resource.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response["Error"]["Code"] == "ResourceNotFoundException":
            # We can't find the resource that you asked for.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
    else:
        # Decrypts secret using the associated KMS CMK.
        # Depending on whether the secret is a string or binary, one of these fields will be populated.
        if "SecretString" in get_secret_value_response:
            secret = get_secret_value_response["SecretString"]
        # else:
        #     decoded_binary_secret = base64.b64decode(
        #         get_secret_value_response["SecretBinary"]
        #     )

    return secret


def insert_prediction(params, result):
    """ insert a new prediction  """

    # convert the SecretString into a dictionary
    params = eval(params)

    latitude = result["payload"][0]
    longitude = result["payload"][1]
    discovery_date = result["payload"][2]
    fire_size = result["payload"][3]
    state_cat = result["payload"][4]
    owner_descr_cat = result["payload"][5]
    discovery_day_of_week_cat = result["payload"][6]
    stat_cause_descr = result["prediction_label"]
    max_probability = result["prediction_probability"]

    sql = """INSERT INTO public.predictions(latitude, longitude, discovery_date, fire_size, state_cat, owner_descr_cat, discovery_day_of_week_cat, stat_cause_descr, max_probability)
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id;"""

    # sql = """SELECT * FROM public.predictions;"""

    conn = None

    try:

        # connect to the PostgreSQL database
        conn = psycopg2.connect(
            database=params["dbname"],
            user=params["username"],
            password=params["password"],
            host=params["host"],
            port=params["port"],
        )

        # create a new cursor
        cur = conn.cursor()

        # execute the INSERT statement
        cur.execute(
            sql,
            (
                latitude,
                longitude,
                discovery_date,
                fire_size,
                state_cat,
                owner_descr_cat,
                discovery_day_of_week_cat,
                stat_cause_descr,
                max_probability,
            ),
        )

        id = cur.fetchone()[0]

        # get the generated id back
        # prediction_records = cur.fetchall()

        # for row in prediction_records:
        #     print(row)

        # commit the changes to the database
        conn.commit()

        # close communication with the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            cur.close()
            conn.close()

    return id


if __name__ == "__main__":
    params = get_secret()
    insert_prediction(params, result=None)