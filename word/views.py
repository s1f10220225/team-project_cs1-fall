from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
import random
from word.models import Word

# Create your views here.


def top(request):
    return render(request, 'word/top.html')



def list(request):

    context = {
        
    }
    return render(request, "word/list.html", context)



def test(request):
    try:
        word = Word.objects.filter(test_num=test_num, genre=genre)
    except Word.DoesNotExist:
        raise Http404("Word does not exist")
    word_list
    word_list_order = []

    for _ in len(word):
        word_list += random.choice(word)

    now_word = 'a'
    context = {
        'word': word,
        'now_word': now_word
    }
    return render(request, "word/test.html", context)