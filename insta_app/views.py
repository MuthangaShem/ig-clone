from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from insat_app.forms import AuthenticateForm, UserCreateForm, PostForm
from insat_app.models import Post
# Create your views here.


def index(request, auth_form=None, user_form=None):
    # User is logged in
    if request.user.is_authenticated():
        post_form = PostForm()
        user = request.user
        posts_self = Post.objects.filter(user=user.id)
        posts_buddies = Post.objects.filter(user__userprofile__in=user.profile.follows.all)
        posts = posts_self | posts_buddies

        return render(request,
                      'buddies.html',
                      {'post_form': post_form, 'user': user,
                       'posts': posts,
                       'next_url': '/', })
    else:
        # User is not logged in
        auth_form = auth_form or AuthenticateForm()
        user_form = user_form or UserCreateForm()

        return render(request,
                      'home.html',
                      {'auth_form': auth_form, 'user_form': user_form, })
