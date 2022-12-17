from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addsecret/', views.addSecretView, name='addsecret'),
    path('secret/<str:secretkey>/', views.readSecretView, name='readsecret'),
    path('user/<str:user>/', views.userPageView, name='userpage'),
    path('secretpath/', views.secretPathView, name='secretpath')
]