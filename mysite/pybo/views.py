from django.shortcuts import render , get_object_or_404 ,redirect

# Create your views here.

from django.http import HttpResponse
from .models import Question, Answer
from django.utils import timezone

def index(request):
  # return HttpResponse("Hi my name hidden masters!!!#########@@@@@@@@@@@@@#")
  question_list = Question.objects.order_by('-create_date')
  context = {'question_list' : question_list }
  return render(request, 'pybo/question_list.html', context)



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'pybo/question_detail.html', {'question' : question})

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get("content"),create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)
