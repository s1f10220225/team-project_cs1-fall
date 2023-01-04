from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
import random
from word.models import Word, Test

# Create your views here.


def top(request):
    return render(request, "word/top.html")



def list(request):

    context = {

    }
    return render(request, "word/list.html", context)

def genre_select(request):
    word = Word.objects.values_list('genre', flat=True)
    genre_list = dict.fromkeys(word)
    context = {
        'genre_list': genre_list,
    }
    return render(request, "word/test_select.html", context)

def num_select(request, genre):
    word = Word.objects.filter(genre=genre).values_list('test_num', flat=True)
    test_num_list = dict.fromkeys(word)
    list_name_list = []
    for i in test_num_list:
        list_name_list.append(Word.objects.filter(pk=i))

    context = {
        'test_num': test_num_list,
        'list_name' : list_name_list,
        'genre' : genre,
    }
    return render(request, "word/test_select.html", context)

def test(request, genre, test_num):
    try:
        word = Word.objects.filter(test_num=test_num, genre=genre)
    except Word.DoesNotExist:
        raise Http404("Word data does not exist")

    word_id = [] # テスト対象の単語リストの各単語(idで構成)
    word_id_order = [] # 単語テストの順番(idで構成)
    word_options_list = [] # テストの順番で並んだ選択肢リスト
    word_options = [] # 選択肢リスト作成用のリスト(idで構成)

    for i in word:
            word_id.append(i.id)

    word_id_replica = word_id.copy()

# 出題順の決定
    while 0 < len(word_id_replica):
        choice_word_id = random.choice(word_id_replica)
        word_id_order.append(choice_word_id)
        word_id_replica.remove(choice_word_id)

    # 過去のテストデータを削除(時間があれば過去のデータを残しても処理できるようにする)
    test_data = Test.objects.all()
    test_data.delete()
# 出題順に応じた単語、意味リストの作成
    for i in word_id_order:
        word_record = Word.objects.get(pk=i)
        word_id_order_replica = word_id_order.copy()
        word_id_order_replica.remove(i)
        word_options = []
        for _ in range(3):
            word_option = random.choice(word_id_order_replica)
            word_options.append(word_option)
            word_id_order_replica.remove(word_option)
        word_options.append(i)
        word_options = random.sample(word_options, 4)
        word_options_list = []
        for n in word_options:
            word_options_record = Word.objects.get(pk=n)
            word_options_list.append(word_options_record.meaning)
        correct_word = word_record.word
        correct_answer = word_record.meaning
        # 単語や選択肢をテスト用のModelに追加
        test_data = Test(word= correct_word, option1=word_options_list[0], option2=word_options_list[1], option3=word_options_list[2], option4=word_options_list[3], correct_answer=correct_answer)
        test_data.save()

    context = {
        'word': word,
        'test_data': Test.objects.all(),
        'genre' : genre,
        'test_num' : test_num,
    }
    return render(request, "word/test.html", context)

def result(request, genre, test_num):
    try:
        test_data = Test.objects.all()
    except Test.DoesNotExist:
        raise Http404("Test data does not exist")
    if request.method == 'POST':
        cnt = 1
        for i in test_data:
            result = Test.objects.get(pk=i.id)
            result.answer = request.POST[f'{cnt}']
            result.save()
            cnt += 1
    cnt -= 1
    pnt = 0
    for i in test_data:
        result = Test.objects.get(pk=i.id)
        if result.answer == result.correct_answer:
            pnt += 1
    context = {
        'word': Word.objects.filter(test_num=test_num, genre=genre),
        'test_data': Test.objects.all(),
        'point': pnt,
        'full': cnt,
        'genre' : genre,
        'test_num' : test_num,
    }
    return render(request, "word/result.html", context)