from django.shortcuts import render
from .import urls
from django.http import HttpResponse
from django.template import loader
def htmlexample(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def signin(request):
    template=loader.get_template('sign_in.html')
    return HttpResponse(template.render())
def main(request):
    template=loader.get_template('main.html')
    return HttpResponse(template.render())
# Create your views here.
