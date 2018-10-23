from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        url(r'^$', views.stuff, name='stuff'),
        url(r'^signup/$', views.signup, name='signup'),
        url(r'^login/$', views.signin, name='login'),
        url(r'^index/$', views.index, name='index'),
        #url(),  
        
        
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)