from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.index),
	url(r"^users/$", views.index),
	url(r"^users/new/$", views.new),
	url(r'^users/edit/(?P<number>\d+)/$', views.edit),
	url(r'^users/(?P<number>\d+)/$', views.show),
	url(r'^users/create/$',views.create),
	url(r'^users/destroy/(?P<number>\d+)/$', views.destroy),
	url(r'^users/update/(?P<number>\d+)/$', views.update)
]