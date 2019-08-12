from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('food', views.food, name='food'),
    path('login', views.login, name='login'),
    path('sign-in', views.signin, name='signin'),
]