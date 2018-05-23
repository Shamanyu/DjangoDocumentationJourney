# Write views

from django.http import HttpResponse

# Create your views here.

# The first argument is necessarily a HttpRequest object
def index(request):

    return HttpResponse("Hey there, you're at the polls index!")
