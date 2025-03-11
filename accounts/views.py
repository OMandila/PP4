from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def roles (request):
    return HttpResponse("Trumpbot roles!")