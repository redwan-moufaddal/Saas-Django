from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Notes
def home_page_request(request):

    return render(request, 'home.html',{"x":Notes.objects.all()})