import pytest

import lambda_function


@pytest.fixture(params=[
    ("hoge", "KATO", "E231", 10)
])
def regist_error_data(request):
    return {
        "company": request.param[0],
        "maker": request.param[1],
        "series": request.param[2],
        "cars": request.param[3]
    }


def test_validation_error_not_found_company(regist_error_data):
    company = regist_error_data["company"]
    with pytest.raises(ValueError):
        lambda_function.verify_with_company_master_data(company)
