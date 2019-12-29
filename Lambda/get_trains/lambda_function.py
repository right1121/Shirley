import json

import boto3

from api_response import api_response

dynamodb_client = boto3.client('dynamodb')

depot_table_name = 'depot'


def lambda_handler(event, context):
    try:
        return main()
    except ValueError as e:
        print('ValueError error', e)
        return api_response.validation_error()
    except Exception as e:
        print('Exception error', e)
        return api_response.exception_error()


def main():
    response = api_response()

    res = query_ownership_train_cars(depot_table_name)

    response.body = res

    return response.format()


def query_ownership_train_cars(table_name):
    res = dynamodb_client.query(
        TableName=depot_table_name,
        KeyConditions={
            'owner_id': {
                'ComparisonOperator': 'EQ',
                'AttributeValueList': [
                    {'S': 'hogehoge'}
                ]
            }
        }
    )

    train_car_items = res['Items']

    dict_key = "train_id"

    cars_info_dict = convert_query_response_items_to_dict(
        train_car_items, dict_key)

    return cars_info_dict


def convert_query_response_items_to_dict(query_response_items, dict_key):
    converted_data = {
        'Items': [],
        'KeyList': [],
    }

    for train_data in query_response_items:
        item_dict = {}
        for data_key, data_info in train_data.items():
            for data_type, value in data_info.items():
                item_dict[data_key] = convert_type_query_data(data_type, value)

        converted_data['Items'].append(item_dict)
        converted_data['KeyList'].append(item_dict[dict_key])

    return converted_data


def convert_type_query_data(data_type, value):
    if data_type == "S":
        converted_value = value
    elif data_type == "N":
        converted_value = int(value)

    return converted_value
