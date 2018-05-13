from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.index, name='home'),  # root
    url(r'^login$', views.login_view, name='login'),  # login
    url(r'^logout$', views.logout_view, name='logout'),  # logout
    url(r'^signup$', views.signup, name='signup'),  # signup
    url(r'^submit$', views.submit, name='submit'),  # submit new post
    url(r'^users/$', views.users, name='users'),
    url(r'^users/(?P<username>\w{0,30})/$', views.users),
    url(r'^follow$', views.follow),
]
