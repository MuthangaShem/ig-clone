from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from insat_app.forms import AuthenticateForm, UserCreateForm, PostForm
from insat_app.models import Post
# Create your views here.
