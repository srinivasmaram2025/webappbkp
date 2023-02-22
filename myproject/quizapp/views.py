from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def admin(request):
     return render(request, 'quizapp/index.html')
def register(register):
     return render(register, 'quizapp/register.html')
def login(login):
     return render(login, 'quizapp/login.html')    
