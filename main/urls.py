from django.urls import path
from . import views
# from .views import home, about_us

urlpatterns = [
    path('', views.home, name="home"),
    path('emp_detail/<int:pk>/', views.emp_detail, name="emp_detail")
] 