from django.shortcuts import render
from django.http import HttpResponse


def get_info(request):
    return HttpResponse("Hello Joxon")


def get_info_1(request):
    return HttpResponse("Whats up")

# Create your views here.
