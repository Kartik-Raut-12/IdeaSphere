from django.urls import path
from . import views

app_name = 'apis'

urlpatterns = [
    # path('hello', views.hello, name='hello'),
    # path('hello1', views.hello1, name='vinit'),
    path('my_api_endpoint', views.my_api_endpoint, name='my_api_endpoint'),
    path('getFromOpenAI', views.getFromOpenAI, name='getFromOpenAI'),
    path('saveInDatabase', views.saveInDatabase, name='saveInDatabase'),

    path('getAddition', views.getAddition, name='getAddition'),
]