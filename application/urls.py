from django.urls import path
from . import views
#url configuration
urlpatterns = [
    path('', views.say_hello,name='home'),
    path('/about', views.about,name='about'),
]