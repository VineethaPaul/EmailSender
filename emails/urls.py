from django.urls import path
from . import views
urlpatterns = [
    path('Email/',views.SendEmail,name='SendEmail')
]