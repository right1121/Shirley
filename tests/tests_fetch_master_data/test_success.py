import os
import json

from jsonschema import validate

import lambda_function


def read_schema_file():
    path = os.path.join(os.path.dirname(__file__), './schema.json')

    with open(path) as f:
        schema = json.load(f)
    return schema


def test_response_structure():
    res = lambda_function.main()
    res_body = json.loads(res["body"])

    schema = read_schema_file()

    validate(res_body, schema)
