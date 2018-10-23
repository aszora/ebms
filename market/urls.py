from django.conf.urls import url, include
from . import views

urlpatterns = [
        url(r'^$', views.stuff, name='stuff'),
        #url(r'^signup/$', views.signup, name='signup'),
       # url(r'^login/$', views.signin, name='login'),
        #url(),  
        
        
        ]
