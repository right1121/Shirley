import json

import boto3

from api_response import api_response
from common import generate_id

dynamodb_client = boto3.client('dynamodb')

train_table_name = "train"


def lambda_handler(event, context):
    body = json.loads(event["body"])
    return main(body)


def main(body):
    api = api_response()

    company = body["company"]
    maker = body["maker"]
    series = body["series"]
    cars = str(body["cars"])

    id_ = generate_id()

    item = {
        "id": {"S": id_},
        "company": {"S": company},
        "maker": {"S": maker},
        "series": {"S": series},
        "cars": {"N": cars}
    }

    param = {
        "TableName": train_table_name,
        "Item": item,
        "Expected": {
            "id": {
                "Exists": False
            }
        }
    }

    dynamodb_client.put_item(**param)

    return api.format_response()
