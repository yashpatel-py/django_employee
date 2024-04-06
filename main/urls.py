from django.urls import path
from . import views
# from .views import home, about_us

urlpatterns = [
    path('', views.home, name="home"),
    path('emp_detail/<int:pk>/', views.emp_detail, name="emp_detail"),
    path('emp_create/', views.emp_create, name="emp_create"),
    path('emp_update/<int:pk>/', views.emp_update, name="emp_update"),
] 