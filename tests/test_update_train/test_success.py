import lambda_function


def test_update_record():
    body = {
        "owner_id": "dc2bc5cb-ae06-4288-b64b-8c501ec60867",
        "train_id": "3aa90f87-9a8e-42f9-8759-1295ff5e0c04",
        "company": "東急",
        "part_number": 12345,
    }
    lambda_function.main(body)
