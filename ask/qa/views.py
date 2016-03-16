from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, InvalidPage
from qa.models import Question, Answer

def test(request, *args, **kwargs):
   return HttpResponse('OK')

def new(request):
    questions = Question.objects.order_by("-id")
    limit = request.GET.get('limit',10)
    page = request.GET.get('page',1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '?page='
    page = paginator.page(page)
    return render(request, 'new.html', {
        'questions': page.object_list,
	'page': page, 
	'paginator': paginator,
})

def popular(request):
    questions = Question.objects.order_by("-rating")
    limit = request.GET.get('limit',10)
    page = request.GET.get('page',1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '?page='
    page = paginator.page(page)
    return render(request, 'popular.html', {
        'questions': page.object_list,
	'page': page, 
	'paginator': paginator,
})

def question(request, id):
    question = get_object_or_404(Question, id=id)
    answers = question.answer_set.all()
    answer_form = AnswerForm({"question": question.id})
    return render(request, 'question.html', {
        'question': question,
        'answers': answers,
        'form': answer_form
    })
