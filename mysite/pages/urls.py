from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addsecret/', views.addSecretView, name='addsecret'),
    path('secret/<str:secretkey>/', views.readSecretView, name='readsecret'),
    path('user/<str:user>/', views.userPageView, name='userpage'),
    # The above path for the user could use the user's id instead of
    # their name, so that it couldn't be accessed just by knowing
    # the user's name
    path('secretpath/', views.secretPathView, name='secretpath')
]