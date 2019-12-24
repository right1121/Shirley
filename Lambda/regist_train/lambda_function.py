import json

import boto3

from api_response import api_response
from common import generate_uuid

dynamodb_client = boto3.client('dynamodb')

train_table_name = "depot"
railway_company_table_name = "railway_company"


def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])
        body["owner_id"] = event["requestContext"]["authorizer"]["claims"]["cognito:username"]
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

    owner_id = body["owner_id"]
    company = body["company"]
    maker = body["maker"]
    series = body["series"]
    cars = str(body["cars"])

    id_ = generate_uuid()

    items = {
        "train_id": {"S": id_},
        "company": {"S": company},
        "maker": {"S": maker},
        "series": {"S": series},
        "cars": {"N": cars},
        "owner_id": {"S": owner_id}
    }

    param = {
        "TableName": train_table_name,
        "Item": items,
        "Expected": {
            "id": {
                "Exists": False
            }
        }
    }

    dynamodb_client.put_item(**param)

    response.body = {
        "train_id": id_
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
