import json

import boto3

from api_response import api_response
from common import generate_uuid

dynamodb_client = boto3.client('dynamodb')

depot_table_name = "depot"


def lambda_handler(event, context):
    try:
        return main()
    except ValueError as e:
        print("ValueError error", e)
        return api_response.validation_error()
    except Exception as e:
        print("Exception error", e)
        return api_response.exception_error()


def main():
    response = api_response()

    res = dynamodb_client.query(
        TableName=depot_table_name,
        KeyConditions={
            "owner_id": {
                "ComparisonOperator": "EQ",
                "AttributeValueList": [
                    {"S": "hogehoge"}
                ]
            }
        }
    )

    response.body = {
        "records": res
    }

    return response.format()
