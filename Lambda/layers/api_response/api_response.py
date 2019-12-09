import json


class api_response():
    def __init__(self):
        self.__status_code = 200
        self.__headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Access-Control-Allow-Origin': '*'
        }
        self.__body = {}

    @property
    def status_code(self):
        return self.__status_code

    @status_code.setter
    def status_code(self, _status_code):
        self.__status_code = _status_code

    @property
    def header(self):
        return self.__headers

    @header.setter
    def header(self, _headers):
        self.__headers = _headers

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, _body):
        self.__body = _body

    def format_response(self):
        return {
            'statusCode': self.__status_code,
            'headers': self.__headers,
            'body': json.dumps(self.__body)
        }
