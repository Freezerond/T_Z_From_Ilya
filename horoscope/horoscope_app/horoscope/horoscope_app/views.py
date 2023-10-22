from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import *

def main_page(request):
    posts = Zodiac_signs_prognoz.objects.all
    context = {
        'posts': posts,
        'title': 'Гороскоп'
    }
    return render(request, 'horoscope_app/horoscope.html', context=context)

def Zodiac_sign(request, zodiac):
    post = get_object_or_404(Zodiac_signs_prognoz, url=zodiac)

    context = {
        'post': post,
        'title': post.title,
    }

    return render(request, 'horoscope_app/zodiac_signs.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>ERROR404</h1>')
