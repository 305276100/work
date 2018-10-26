# -*-coding:utf-8-*-
from django.conf.urls import url

from OS import views

urlpatterns = [
    url(r"^$", views.index_view),
    url(r'login/', views.login_view)

]
