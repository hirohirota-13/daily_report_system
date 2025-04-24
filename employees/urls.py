from django.urls import path
from . import views
from .views import EmployeeListView

urlpatterns = [
#   path('', views.employee_list, name='employee_index'),
  path('', EmployeeListView.as_view(), name='employee_index'),
  path('new/', views.employee_new, name='employee_new'),
#   path('create/', views.employee_create, name='employee_create'),
  path('<int:pk>/edit/', views.employee_edit, name='employee_edit'),
  path('<int:pk>/update/', views.employee_update, name='employee_update'),
  path('<int:pk>/delete/', views.employee_delete, name='employee_delete'),
  path('<int:pk>/delete_confirm/', views.employee_delete_confirm, name='employee_delete_confirm'),
]
