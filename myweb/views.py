from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout as logout_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import inputmovies

# Create your views here.
def index(req):
    inputmoviess = inputmovies.objects.all()
    return render(req, 'myweb/index.html', {'inputmoviess': inputmoviess})

def signup(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
    context['form']=form
    return render(request,'myweb/signup.html',context)

def logout(req):
    logout_user(req)
    return redirect('login')

def movie(req):
	return render(req,'myweb/movie.html')

def detail(request, question_id):
    return render(request, 'myweb/detail.html')

def insertmovie(request):
    if request.method == 'POST':

        img = request.POST.get("img")
        moviename = request.POST.get("moviename")
        synopsis = request.POST.get("synopsis")
        add = inputmovies(img=img,moviename=moviename,synopsis=synopsis)
        add.save()
        return redirect('index')
    return render(request, 'myweb/insertmovie.html')

def insertmovies(req):
    inputmoviess = inputmovies.objects.all()
    ins = {
        'inputmoviess' : inputmoviess
        }
    return render(req, 'myweb/insertmovie.html', ins)