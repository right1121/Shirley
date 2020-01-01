import json

import boto3

from api_response import api_response


def lambda_handler(event, context):
    try:
        return main()
    except Exception as e:
        print("Exception error", e)
        return api_response.exception_error()


def main():
    pass
