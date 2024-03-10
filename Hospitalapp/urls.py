from django.urls import path
from . import views
app_name='hos' 
urlpatterns = [
    path('',views.Home,name='home'),
]
