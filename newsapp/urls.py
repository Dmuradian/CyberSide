from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='newsapp-home'),
    path('user/', views.user, name='newsapp-user'),
    # path('about/', views.about, name='myfirstapp-about')
    # path('', views.home, name='myfirstapp-home')
]