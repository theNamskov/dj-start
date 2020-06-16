from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('more-info', views.more_info, name="more-info"),
]
