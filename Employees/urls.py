from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.employeeList.as_view(), name = 'employeeList'),
    path('search/',views.employeeSearch, name = 'employeeSearch')    
]
