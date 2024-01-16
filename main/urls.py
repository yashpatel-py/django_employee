from django.urls import path
from . import views
# from .views import home, about_us

urlpatterns = [
    path('', views.home, name="home"),
    path('about_us/', views.about_us, name="home")
] 