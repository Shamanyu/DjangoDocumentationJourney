# Write views

from django.http import HttpResponse

# Create your views here.

def index(request):

    return HttpResponse("Hey there, you're at the polls index!")
