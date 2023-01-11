from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from polls.models import Choice,Question
import datetime

def current_datetime(request):
  now = datetime.datetime.now()
  html = "<html><body>It is now %s.</body></html>" % now
  return HttpResponse(html)

def index(request):
  latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
  context = {'latest_question_list':latest_question_list}
  return render(request,'polls/index.html',context)
# Create your views here.

def detail(request,question_id):
  question = get_object_or_404(Question,pk=question_id)
  return render(request,'polls/detail.html',{'question':question})

def vote(request,question_id):
  question = get_object_or_404(Question,pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except(KeyError,Choice.DoesNotExist):
    return render(request,'polls/detail.html',{
      'question:':question,
      'error_message':"You didn't select a choice.",
    })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results',args=(question.id)))
    
def results(request,question_id):
  question = get_object_or_404(Question,pk=question_id)
  return render(request,'polls/results.html',{'question':question})
