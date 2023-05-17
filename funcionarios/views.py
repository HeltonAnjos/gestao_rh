from django.urls import reverse_lazy
from django .views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario
from django.contrib.auth.models import User


class FuncionarioList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['name', 'departamentos']


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['name', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.name.split(' ')[0] + funcionario.name.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)
        