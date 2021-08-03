from django.conf.urls import url
from myWebApp import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
		url(r'^api/users$', views.users_list),
		url(r'^api/users/(?P<pk>[0-9]+)$', csrf_exempt(views.user_detail)),
		url(r'^api/users/(?P<pk>[0-9]+)$', csrf_exempt(views.user_delete)),
		]