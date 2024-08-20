from django.urls import path
from . import views

urlpatterns = [
    # path('addemployee/', views.add_employee, name='addemployee'),
    path('add_emp', views.add_employ, name='add_emp'),
    path('delete_emp/<int:pk>/', views.delete_emp, name='delete_emp'), # <int:pk> - is the key that we have passed to delete in the url 
    path('edit_emp/<int:pk>/', views.edit_emp, name='edit_emp'),
]
