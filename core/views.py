from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def error_handler (request):
    return HttpResponse("Trumpbot core!")