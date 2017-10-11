from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^authors/$', views.AuthorList.as_view()),
    url(r'^authors/(?P<pk>[0-9]+[a-z]+[A-Z])/$', views.AuthorDetail.as_view()),
]