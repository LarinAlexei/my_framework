from jinja2 import Template
from os.path import join
from jinja2 import FileSystemLoader
from jinja2.environment import Environment


def render(template_name, folder='templates', **kwargs):
    """
    Эта функция выполняет рендеринг шаблона по переданному контексту
    :param template_name: Имя шаблона
    :param folder: Каталог, с нашими шаблонами
    :param kwargs: Параметр контекста
    :return:
    """
    env = Environment()
    # Указываем папку для поиска шаблона
    env.loader = FileSystemLoader(folder)
    # Передаем контекст в найденный шаблон
    template = env.get_template(template_name)
    return template.render(**kwargs)
