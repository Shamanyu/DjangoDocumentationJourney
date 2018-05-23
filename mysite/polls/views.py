# Write views

from django.http import HttpResponse, HttpResponseRedirect
"""
get_object_or_404 either returns an object or raises Http404, passing the
optional keyword arguments to 'get' method.
get_list_or_404 either returns a list or raises Http404, passing the
optional keyword arguments to 'filter' method.
"""
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse

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

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

    """ Always return an HttpResponseRedirect after successfully dealing with
    POST data. This prevents data from being posted twice if a user hits the
    'back' button. Moreover, use 'reverse' to build redirect url to prevent
    hardcoding
    """
    return HttpResponseRedirect(reverse('polls:results', args=(question_id, )))
