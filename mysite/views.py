# Author: Pratyush-Harsh
#Organzition : BIT Mesra
'''
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello World Pratyush</h1>")

def about(request):
    return HttpResponse("<h1> About Pratyush</h1>")
'''

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    param = {'name':'harry potter','teacher':'Mr Snapes'}
    return render(request,'index.html',param)
def about(request):
    return HttpResponse("about");

def removepunc(request):
    return HttpResponse("remove punc");


def newlineremove(request):
    return HttpResponse("newlineremove");

def capfirst(request):
    return HttpResponse("cap first");



def spaceremove(request):
    return HttpResponse("spaceremove");

def charcount(request):
    return HttpResponse("charcount");


