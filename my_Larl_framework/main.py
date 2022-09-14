from quopri import decodestring
from .myrequests import GetRequests, PostRequests


# Код ошибки 404 - сервер не может найти запрашиваемый Вами ресурс
class PageNotFound404:
    def __call__(self, request):
        return '404 PAGE Found', '404 PAGE Not Found'


class Framework:
    """ Основной класс """

    def __init__(self, routes_obj: dict, fronts_obj: list):
        """
        Основной класс
        :param routes_obj: маршрут в виде словаря
        :param fronts_obj: список функций фронт-контроллера
        """
        self.routes_list = routes_obj
        self.fronts_obj = fronts_obj

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        # если клиент делает запрос без слеша, то добавляем его автоматически
        path += '' if path.endswith('/') else '/'

        request = {}
        # получаем все данные запроса
        method = environ['REQUEST_METHOD']
        request['method'] = method
        print(method)
        pass
        # TODO добавить обработку запроса с JSON  в теле
        if method == 'POST':
            # получили какие-то параметры из запроса
            data = PostRequests().get_request_params(environ)
            request['data'] = {}
            if data:
                request['data'] = Framework.decode_value(data)
                print(f'post-запрос получен: {Framework.decode_value(data)}')
            # TODO добавим получение файлов

        if method == 'GET':
            request_params = GetRequests().get_request_params(environ)
            request['request_params'] = {}
            if request_params:
                request['request_params'] = Framework.decode_value(request_params)
                print(f'get-запрос получен: {Framework.decode_value(request_params)}')

        # поиск контроллера под полученный нами path
        if path in self.routes_list:
            view = self.routes_list[path]
        else:
            view = PageNotFound404()
        # заполнение requesta данными
        for front in self.fronts_list:
            front(request)
        # запуск контроллера с объектом request
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace('+', ''), 'utf-8')
            val_decode_str = decodestring(val).decode('utf-8')
            new_data[k] = val_decode_str
        return new_data
