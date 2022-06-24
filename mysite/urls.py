from .views import *
from django.urls import path

app_name = 'django'

urlpatterns = [
    path('', index, name='home'),
    path('comment/', login , name='form'),
    path('chart/', chart, name='chart'),
    path('addchart/', addchart, name='addchart')
]