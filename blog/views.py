from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Author

# Create your views here.
def authors(request):
    allauthors = Author.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'allauthors' : allauthors,
    }
    return HttpResponse (template.render(context, request))

