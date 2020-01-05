import json
import os

import pytest
from jsonschema import validate

import lambda_function
from api_response import api_response


def required_item():
    return {
        "owner_id": "hogehoge",
        "company": "東急",
        "maker": "KATO",
        "series": "E231",
        "cars": 10,
        "case_count": 1,
    }


def optional_item():
    item = required_item()
    optional_item = {
        "part_number": "10-1246",
        "lot": 2019,
        "memo": "備考",
    }
    item.update(optional_item)
    return item


@pytest.fixture(params=["required", "optional"])
def params_variation(request):
    pattern = request.param
    if pattern == "required":
        return required_item()
    elif pattern == "optional":
        return optional_item()


def read_schema_file():
    path = os.path.join(os.path.dirname(__file__), './schema.json')

    with open(path) as f:
        schema = json.load(f)
    return schema


def test_response_setting(params_variation):
    body = params_variation
    res = lambda_function.main(body)
    assert res['statusCode'] == 200
    assert res['headers']['Content-Type'] == 'application/json; charset=utf-8'
    assert res['headers']['Access-Control-Allow-Origin'] == '*'


def test_insert_data(params_variation):
    body = params_variation
    res = lambda_function.main(body)

    assert res['statusCode'] == 200

    res_body = json.loads(res["body"])
    schema = read_schema_file()
    validate(res_body, schema)


def test_lambda_handler(params_variation):
    body = params_variation
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
