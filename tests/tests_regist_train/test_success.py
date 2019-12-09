import lambda_function


def test_success():
    res = lambda_function.main()
    assert res["statusCode"] == 200
