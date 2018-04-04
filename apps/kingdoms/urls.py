from django.conf.urls import  url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^maps$', views.maps, name='maps'),
	url(r'^characters$', views.characters, name='characters'),
]