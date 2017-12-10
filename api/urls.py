from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^authors/$', views.AuthorList.as_view()),
    url(r'^authors/(?P<pk>[0-9]+)/$', views.AuthorDetail.as_view()),
    url(r'^users/$', views.MemberList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.MemberDetail.as_view()),
    url(r'^books/$', views.BookList.as_view()),
    url(r'^books/(?P<pk>[0-9]+)/$', views.BookDetail.as_view()),
    url(r'^rents/$', views.RentList.as_view()),
    url(r'^rents/(?P<pk>[0-9]+)/$', views.RentDetail.as_view()),
    url(r'^api-token-auth/', views.CustomObtainAuthToken.as_view()),
    url(r'^current-user/$', views.CurrentUserView.as_view()),
]