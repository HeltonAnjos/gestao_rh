from django.urls import path
from .views import RegistroHoraExtraList, RegistroHoraExtraEdit, RegistroHoraExtraDelete, RegistroHoraExtraCreate, RegistroHoraExtraEditBase, UtilizouHoraExtra, NaoUtilizouHoraExtra

urlpatterns = [
    path('list/', RegistroHoraExtraList.as_view(), name='list_horaextra'),
    path('novo/', RegistroHoraExtraCreate.as_view(), name='create_horaextra'),
    path('editar/<int:pk>/', RegistroHoraExtraEdit.as_view(), name='update_horaextra'),
    path('editarbase/<int:pk>/', RegistroHoraExtraEditBase.as_view(), name='update_horaextrabase'),
    path('utilizou-hora-extra/<int:pk>/', UtilizouHoraExtra.as_view(), name='utilizou_hora_extra'),
    path('nao-utilizou-hora-extra/<int:pk>/', NaoUtilizouHoraExtra.as_view(), name='nao_utilizou_hora_extra'),
    path('deletar/<int:pk>/', RegistroHoraExtraDelete.as_view(), name='delete_horaextra'),
]