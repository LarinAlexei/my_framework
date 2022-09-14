import cgi
import os


class GetRequests:
    @staticmethod
    def parse_input_data(data: str):
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = v
            return result

    @staticmethod
    def get_request_params(environ):
        # получим параметры запроса
        query_string = environ['QUERY_STRING']
        # преобразовываем данные в словар
        request_params = GetRequests.parse_input_data(query_string)
        return request_params


class PostRequests:
    @staticmethod
    def parse_input_data(data: str):
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = v
            return result

    @staticmethod
    def get_wsgi_input_data(environ) -> bytes:
        content_length_data = environ.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        # если данные получены, то их считывают
        data = environ['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            print(f'строка получена после декодирования - {data_str}')
            # преобразовываем данные в словарь
            result = self.parse_input_data(data_str)
        return result

    def get_request_params(self, environ):
        print('отработал правильно')
        # данные на выходе
        data = self.get_wsgi_input_data(environ)
        print(data)
        # преобразовываем данные в словарь
        data = self.parse_wsgi_input_data(data)
        print(data)
        return data
