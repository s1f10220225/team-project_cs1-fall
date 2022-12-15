from django.shortcuts import render, redirect

# Create your views here.


def top(request):
    return render(request, 'word/top.html')
