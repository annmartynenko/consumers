from django.urls import path
from . import views

app_name = 'balance'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
]
