import json

import boto3

from api_response import api_response
from common import generate_id

dynamodb_client = boto3.client('dynamodb', endpoint_url="http://localhost:8000")

train_table_name = "train"
railway_company_table_name = "railway_company"


def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])
        return main(body)
    except ValueError as e:
        print("ValueError error", e)
        return api_response.validation_error()
    except Exception as e:
        print("Exception error", e)
        return api_response.exception_error()


def main(body):
    response = api_response()

    verify_body_data(body)

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

    response.body = {
        "id": id_
    }

    return response.format()


def verify_body_data(body):
    """bodyのデータが妥当か検証する

    :param body: Request Body
    :type body: dict
    """

    verify_with_company_master_data(body["company"])


def verify_with_company_master_data(company):
    """会社名がマスタデータと一致しているか検証する

    :param company: [description]
    :type company: [type]
    """

    company_data = dynamodb_client.get_item(
        TableName=railway_company_table_name,
        Key={
            "name": {
                'S': company
            }
        }
    )
    item = company_data.get('Item', {})

    if len(item) == 0:
        raise ValueError
