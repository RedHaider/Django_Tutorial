from django.urls import path
from .views import Home, AddEmployee , Delete_Employee , EditEmployee

urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('addemployee/',AddEmployee.as_view(), name='addemployee'),
    path('deleteemployee/', Delete_Employee.as_view(), name='deleteemployee'),
    path('editemployee/<int:id>/', EditEmployee.as_view(), name='editemployee')
]  