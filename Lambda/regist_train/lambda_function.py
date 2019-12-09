import json

import boto3

from api_response import api_response

client = boto3.client('dynamodb')


def lambda_handler(event, context):
    body = json.loads(event["body"])
    return main(body)


def main(body):
    api = api_response()

    company = body["company"]
    maker = body["maker"]
    series = body["series"]
    cars = body["cars"]

    return api.format_response()
