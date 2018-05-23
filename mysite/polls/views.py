# Write views

from django.http import HttpResponse
"""
get_object_or_404 either returns an object or raises Http404, passing the
optional keyword arguments to 'get' method.
get_list_or_404 either returns a list or raises Http404, passing the
optional keyword arguments to 'filter' method.
"""
from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Question

# Create your views here.

# The first argument is necessarily a HttpRequest object
def index(request):

    latest_question_list = get_list_or_404(Question)[:5]
    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'polls/index.html', context)

def detail(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):

    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):

    return HttpResponse("You're voting on question %s." % question_id)
