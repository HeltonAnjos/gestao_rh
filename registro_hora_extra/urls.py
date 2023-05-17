from django.urls import path
from .views import RegistroHoraExtraList, RegistroHoraExtraEdit, RegistroHoraExtraDelete, RegistroHoraExtraCreate

urlpatterns = [
    path('list/', RegistroHoraExtraList.as_view(), name='list_horaextra'),
    path('novo/', RegistroHoraExtraCreate.as_view(), name='create_horaextra'),
    path('editar/<int:pk>/', RegistroHoraExtraEdit.as_view(), name='update_horaextra'),
    path('deletar/<int:pk>/', RegistroHoraExtraDelete.as_view(), name='delete_horaextra'),
]