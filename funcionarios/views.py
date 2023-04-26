from django.views.generic import View
from .models import Funcionario
from django.http import HttpResponse    


def Home(request):
    return HttpResponse('olá')
#class Home(View):
   # model = Funcionario
   # template_name = 'index.html'
