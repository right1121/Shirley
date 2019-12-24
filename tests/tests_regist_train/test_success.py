import json

import pytest

import lambda_function
from api_response import api_response


@pytest.fixture
def regist_data():
    return {
        "owner_id": "hogehoge",
        "company": "東急",
        "maker": "KATO",
        "series": "E231",
        "cars": 10
    }


def test_response_setting(regist_data):
    body = regist_data
    res = lambda_function.main(body)
    assert res['statusCode'] == 200
    assert res['headers']['Content-Type'] == 'application/json; charset=utf-8'
    assert res['headers']['Access-Control-Allow-Origin'] == '*'


def test_insert_data(regist_data):
    body = regist_data
    res = lambda_function.main(body)

    assert res['statusCode'] == 200


def test_lambda_handler(regist_data):
    body = regist_data
    event = {
        "body": json.dumps(body),
        "requestContext": {
            "authorizer": {
                "claims": {
                    "cognito:username": "pytest"
                }
            }
        }
    }
    context = {}
    res = lambda_function.lambda_handler(event, context)
    body = json.loads(res["body"])
    train_id = body.get("train_id")
    assert res['statusCode'] == 200
    assert res['headers']['Content-Type'] == 'application/json; charset=utf-8'
    assert res['headers']['Access-Control-Allow-Origin'] == '*'
    assert train_id is not None
