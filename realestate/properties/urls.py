from django.urls import path
from . import views



app_name= 'properties'

urlpatterns = [
    path('', views.properties, name="propertiesView"),
    path('<int:homes_id>', views.propertie_detail, name='detail')
]
