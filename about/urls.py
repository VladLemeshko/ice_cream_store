from django.urls import path

from . import views

app_name = 'about'

urlpatterns = [
    path('', views.DescriptionPage.as_view(), name='description'),
]