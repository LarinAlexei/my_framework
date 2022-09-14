from datetime import date
from views import Index, About, Expertize, Onsite_examination


# фронт контроллер
def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/index': Index(),
    '/about/': About(),
    '/expertize/': Expertize(),
    '/onsite_examination/': Onsite_examination(),
}
