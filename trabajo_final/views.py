# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response

# Create your views here.

def index (request):
    """ view principal
    """
    return render_to_response('index.html')

def contact (request):
    """ view principal
    """
    return render_to_response('contact.html')


def about (request):
    """view del acerca de ...
    """
    return render_to_response('about.html')

def login (request):
    """view del login
    """
    return render_to_response('login.html')

def search(request):
    """view de los resultados de busqueda
    """
    return render_to_response('login.html')


def post (request):
    return render_to_response('post.html')