from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^leach/$', views.index, name='leach'),
	url(r'^signout/$', views.signout, name='signout'),
]
