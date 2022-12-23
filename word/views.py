from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
import random
from word.models import Word, Test

# Create your views here.


def top(request):
    return render(request, 'word/top.html')

def test(request, test_num, genre):
    try:
        word = Word.objects.filter(test_num=test_num, genre=genre)
    except Word.DoesNotExist:
        raise Http404("Word does not exist")

    word_id = []
    word_id_order = []
    word_options_list = []

    for i in range(word.id):
            word_id += i

    word_id_replica = word_id.copy()

    while 0 < len(word_id_replica):
        choice_word_id = random.choice(word_id_replica)
        word_id_order += choice_word_id
        word_id_replica -= choice_word_id

    for i in word_id_order:
        word_list = Word.objects.get(pk=i)
        word_list
        word_list


    context = {
        'test_data': word,
    }
    return render(request, "word/test.html", context)