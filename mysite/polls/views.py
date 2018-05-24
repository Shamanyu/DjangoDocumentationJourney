# Write views

from django.http import HttpResponseRedirect
"""
get_object_or_404 either returns an object or raises Http404, passing the
optional keyword arguments to 'get' method.
get_list_or_404 either returns a list or raises Http404, passing the
optional keyword arguments to 'filter' method.
"""
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

# Create your views here.

# ListView displays a list of objects
# The default template used by IndexView is <app_name>/<model_name>_list.html
# It's better to always still explicitly specify the template name
class IndexView(generic.ListView):

    template_name = 'polls/index.html'
    # Over-ride the default context_object_name 'question_list'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

# DetailView expects the primary key captured to be called 'pk'
# The default template used by DetailView is <app_name>/<model_name>_detail.html
class DetailView(generic.DetailView):

    # Default context_object_name is 'question'
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):

    model = Question
    template_name = 'polls/results.html'

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
