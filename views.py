from my_Larl_framework.templator import render

# TODO Данные вынесены в отдельные файлы - убрать после добавления в нашу БД
from data_false import nav_menu, objects_data


class BaseView:
    """Класс при наследовании позволяет добавить возможность передачи имени
    нужного шаблона при определении маршрута и передать в контекст контроллера имя раздела.
    Если значение не передается, то принимается значение вида [имя класса в нижнем регистре].htm"""

    def __init__(self, template_name=None):
        super(BaseView, self).__init__()
        # имя шаблона
        self.template_name = template_name if template_name else f'{self.__class__.__name__.lower()}.html'
        # базовое состояние передаваемого контекста в шаблон
        self.context = {
            'site_section': self.template_name.split('.')[0],
            'nav_menu': nav_menu,
        }


# Разделы сайта.
class Index(BaseView):
    def __call__(self, request):
        self.context['info'] = 'Информация о нашей компании.'
        return '200 OK', render(self.template_name, context=self.context)


class Expertize(BaseView):
    def __call__(self, request):
        self.context['info'] = 'Закажите экспертизу у нас!'
        return '200 OK', render(self.template_name, context=self.context)


class Onsite_examination(BaseView):
    def __call__(self, request):
        self.context['info'] = 'Закажите выездную экспертизу, от нашего лучшего специалиста!'
        return '200 OK', render(self.template_name, context=self.context)
