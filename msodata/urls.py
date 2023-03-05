from django.urls import path
from . import views
urlpatterns = [
    path('MSO/',views.msoData,name='msoData'),
    path('MSO/msoDataUploadView',views.msoDataUploadView,name='msoDataUploadView')
]