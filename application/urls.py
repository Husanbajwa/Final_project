from django.urls import path
from . import views
#url configuration
urlpatterns = [
    path('', views.home,name='home'),#To index.html
    path('home/', views.home,name='home'),
    path('contact/', views.contact),
    path('about/', views.about),
]