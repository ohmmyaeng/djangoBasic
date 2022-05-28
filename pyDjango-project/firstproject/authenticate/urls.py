from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),   
    path('signout', views.signout, name='signout'),
    path('', views.home, name='home'),
    path('data', views.data, name='data'),
]
