from django.shortcuts import render , HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('<h1>hello</h1>')
