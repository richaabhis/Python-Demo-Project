from django.urls import path

from . import views

urlpatterns = [
    path('', views.INDEX, name='home'),
    path('addEmployee', views.addEmployee, name='addEmployee'),
    path('editEmployee', views.editEmployee, name='editEmployee'),
    path('updateEmployee/<str:id>', views.updateEmployee, name='updateEmployee'),
    path('deleteEmployee/<str:id>', views.deleteEmployee, name='deleteEmployee'),
]
