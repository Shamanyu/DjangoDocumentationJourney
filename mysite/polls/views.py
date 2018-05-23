# Write views

from django.http import HttpResponse

# Create your views here.

# The first argument is necessarily a HttpRequest object
def index(request):

    return HttpResponse("Hey there, you're at the polls index!")

def detail(request, question_id):

    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):

    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):

    return HttpResponse("You're voting on question %s." % question_id)
