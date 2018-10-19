from django.conf.urls import url, include
from . import views

urlpatterns = [
        url(r'^$', views.stuff, name='stuff'),
        #url(),  
        
        
        ]
