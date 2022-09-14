from wsgiref.simple_server import make_server
from my_Larl_framework.main import Framework
from urls import routes, fronts


URL = 'localhost'
PORT = 8080

application = Framework(routes, fronts)


with make_server('', PORT, application) as httpd:
    print(f'Сервер запущен на порту ${PORT}..\n', f"http://{URL}:{PORT}")
    httpd.serve_forever()
