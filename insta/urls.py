"""insta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from insta_app import views as app_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^', include('insta_app.urls')),
    url(r'^$', app_views.index, name='home'),  # root
    url(r'^login$', app_views.login_view, name='login'),  # login
    url(r'^logout$', app_views.logout_view, name='logout'),  # logout
    url(r'^signup$', app_views.signup, name='signup'),  # signup
    url(r'^submit$', app_views.submit, name='submit'),  # submit new post
    url(r'^users$', app_views.users, name='users'),
    url(r'^users(?P<username>\w{0,30})/$', app_views.users),
    url(r'^follow$', app_views.follow),
]
