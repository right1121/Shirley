import pytest

import lambda_function


@pytest.fixture
def regist_data():
    return {
        "company": "JR東",
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
