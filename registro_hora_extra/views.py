from django.urls import reverse_lazy
from django .views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm


class RegistroHoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class RegistroHoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'funcionario', 'horas']


class RegistroHoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_horaextra')


class RegistroHoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(RegistroHoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
