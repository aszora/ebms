
from django.conf.urls import patterns, url, include
from . import views
urlpatterns = [
        url(r'^signup/$', views.signup, name='signup'),
        url(r'^login/$', views.signin, name='login'),
        #url(),  
        
        
        ]
