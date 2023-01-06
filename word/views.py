from django.shortcuts import render, redirect
from django.http import Http404
import random
from word.models import Genre, Listinfo, Word, Test

# Create your views here.


def top(request):
    return render(request, "word/top.html")


def list(request, belong):
    try:
        word = Word.objects.filter(belonging_list_id=belong)
    except Word.DoesNotExist:
        raise Http404("Word data does not exist")

    info = Listinfo.objects.get(pk=belong)

    context = {
        'words': word,
        'info': info,
        'genre': Genre.objects.get(pk=info.genre_id),
        'add_num': [i+1 for i in range(20)]
    }
    return render(request, "word/list.html", context)

def genre_list(request):
    try:
        genre = Genre.objects.all()
    except Genre.DoesNotExist:
        return redirect(f"http://127.0.0.1:8000/word/first/list_select")
    context = {
        'genre_list': genre,
    }
    return render(request, "word/list_select.html", context)

def name_list(request, genre):
    context = {
        'genre_list': Genre.objects.get(pk=genre),
        'info': Listinfo.objects.filter(genre_id=genre).order_by('list_num'),
    }
    try:
        return render(request, "word/list_select.html", context)
    except TypeError:
        return redirect(f"http://127.0.0.1:8000/word/first/list_select/{genre}")

def first_genre_select(request):
    return render(request, "word/first_list_select.html")

def first_list_select(request, genre):
    context = {
        'genre_list': Genre.objects.get(pk=genre),
    }
    return render(request, f"word/first_list_select.html", context)
    
def cd_genre(request):
    context = {
        'genre': Genre.objects.all(),
    }
    return render(request, "word/cd_genre.html", context)

def create_genre(request):
    if request.method == 'POST':
            genre = Genre(genre=request.POST['name'])
            genre.save()
    return redirect(f"http://127.0.0.1:8000/word/cd_genre")

def genre_delete(request, genre):
    genre = Genre.objects.get(pk=genre)
    genre.delete()
    return redirect(f"http://127.0.0.1:8000/word/cd_genre")


def cd_list(request, genre):
    context = {
        'genre': genre,
        'info': Listinfo.objects.filter(genre_id=genre).order_by('list_num'),
    }
    return render(request, "word/cd_list.html", context)

def create_list(request, genre):
    if request.method == 'POST':
            list = Listinfo(genre_id=genre, list_num=request.POST['num'], list_name=request.POST['name'])
            list.save()
    return redirect(f"http://127.0.0.1:8000/word/cd_list/{genre}")

def list_delete(request, genre, id):
    list = Listinfo.objects.get(pk=id)
    list.delete()
    return redirect(f"http://127.0.0.1:8000/word/cd_list/{genre}")


def word_edit(request, word_num, belong):
    try:
        word = Word.objects.get(pk=word_num)
    except Word.DoesNotExist:
        raise Http404("Word data does not exist")

    if request.method == 'POST':
        word.word = request.POST['word']
        word.meaning = request.POST['meaning']
        word.save()
        return redirect(f"http://127.0.0.1:8000/word/list/{belong}")

    context = {
        'word': word,
        'info': belong,
    }
    return render(request, "word/word_edit.html", context)

def word_add(request, belong):
    if request.method == 'POST':
        select = int(request.POST['select_num'])

    context = {
        'info': belong,
        'select_lst': [i for i in range(select)],
        'select': select,
    }
    return render(request, "word/word_add.html", context)

def word_update(request, belong, select):
    if request.method == 'POST':
        for s in [i for i in range(select)]:
            word = Word(word=request.POST[f'word{s}'], meaning=request.POST[f'meaning{s}'], belonging_list_id=belong)
            word.save()

    return redirect(f"http://127.0.0.1:8000/word/list/{belong}")


def word_delete(request, word_num, belong):
    try:
        word = Word.objects.get(pk=word_num)
    except Word.DoesNotExist:
        raise Http404("Word data does not exist")

    word.delete()

    return redirect(f"http://127.0.0.1:8000/word/list/{belong}")


def genre_select(request):
    context = {
        'genre_list': Genre.objects.all(),
    }
    return render(request, "word/test_select.html", context)

def num_select(request, genre):
    context = {
        'genre_list': Genre.objects.get(pk=genre),
        'info': Listinfo.objects.filter(genre_id=genre).order_by('list_num','list_name'),
    }
    return render(request, "word/test_select.html", context)

def test(request, belong):
    try:
        word = Word.objects.filter(belonging_list_id=belong)
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
    
    test = Test.objects.all()
    cnt = 0
    for _ in test:
        cnt += 1
    if cnt < 4:
        return redirect(f"http://127.0.0.1:8000/word/test/{info.id}/error")
    
    info = Listinfo.objects.get(pk=belong)
    genre = Genre.objects.get(pk=info.genre_id)
    context = {
        'word': word,
        'test_data': test,
        'info': info,
        'genre': genre,
    }
    return render(request, "word/test.html", context)

def test_error(request, belong):
    try:
        word = Word.objects.filter(belonging_list_id=belong)
    except Word.DoesNotExist:
        raise Http404("Word data does not exist")

    info = Listinfo.objects.get(pk=belong)

    context = {
        'words': word,
        'info': info,
        'genre': Genre.objects.get(pk=info.genre_id),
        'add_num': [i+1 for i in range(20)]
    }
    return render(request, "word/test_error.html", context)


def result(request, belong):
    try:
        test_data = Test.objects.all()
    except Test.DoesNotExist:
        raise Http404("Test data does not exist")
    if request.method == 'POST':
        cnt = 1
        test_data = Test.objects.all()
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
    
    info = Listinfo.objects.get(pk=belong)
    
    context = {
        'word': Word.objects.filter(belonging_list_id=belong),
        'test_data': Test.objects.all(),
        'point': pnt,
        'full': cnt,
        'info': info,
        'genre': Genre.objects.get(pk=info.id),
    }
    return render(request, "word/result.html", context)
