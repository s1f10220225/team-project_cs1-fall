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


#list用関数
def detail(request, Word_id):
	try:
		Word = Word.objects.get(pk=Word_id)
	except Word.DoesNotExist:
		raise Http404("Word does not exist")
		
	context = {
		'Word': Word
	}
	return render(request, "blog/detail.html", context)

def update(request, Word_id):
	try:
		Word = Word.objects.get(pk=Word_id)
	except Word.DoesNotExist:
		raise Http404("Article does not exist")
	if request.method == 'POST':
		Word.word = request.POST['word']
		Word.meaning = request.POST['meaning']
		Word.save()
		return redirect(detail, Word_id)
	context = {
		'Word': Word
	}
	return render(request, "blog/edit.html", context)

def delete(request, Word_id):
	try:
		Word = Word.objects.get(pk=Word_id)
	except Word.DoesNotExist:
		raise Http404("Word does not exist")

	Word.delete()

	return redirect(list3)

def like(request, Word_id):
	try:
		Word = Word.objects.get(pk=Word_id)
		Word.favorite += 1
		Word.save()
	except Word.DoesNotExist:
		raise Http404("Article does not exist")

	return redirect(detail, Word_id)