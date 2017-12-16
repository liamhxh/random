from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    try:
        request.session['counter'] += 1
    except:
        request.session['counter'] = 0

    return render(request,'randomWord/index.html')

def generate(request):
    if request.method == 'POST':
        try:
            request.session['word'] = get_random_string(length=14)
        except:
            request.session['word'] = ''

    return redirect('/')

def reset(request):
    if request.method == 'POST':
        request.session['counter'] = 0
    return redirect('/')