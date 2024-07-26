from django.http import HttpResponse
from django.shortcuts import render,redirect

def home_page_request(request):

    return render(request, 'home.html')