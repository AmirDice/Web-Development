from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from personal.models import Post
from members.forms import EditProfileForm, CommentForm
from teacheco import settings
import requests


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def loadcontent(request):
    try:
        page = request.GET.get('page', 1)
        search = request.GET.get('search', None)
        # url = "https://newsapi.org/v2/everything?q={}&sortBy={}&page={}&apiKey={}".format(
        #     "Technology","popularity",page,settings.APIKEY
        # )
        if search is None or search == "top":
            url = "https://newsapi.org/v2/everything?q=climate-change&apiKey=f90db0776ba540dc8ee7bd468d5f45c0".format(
                "us", page, settings.APIKEY
            )
        else:
            url = "https://newsapi.org/v2/everything?q=climate-change&apiKey=f90db0776ba540dc8ee7bd468d5f45c0".format(
                search, "popularity", page, settings.APIKEY
            )
        print("url:", url)
        r = requests.get(url=url)

        data = r.json()
        if data["status"] != "ok":
            return JsonResponse({"success": False})
        data = data["articles"]
        context = {
            "success": True,
            "data": [],
            "search": search
        }
        for i in data:
            context["data"].append({
                "title": i["title"],
                "description":  "" if i["description"] is None else i["description"],
                "url": i["url"],
                "image": temp_img if i["urlToImage"] is None else i["urlToImage"],
                "publishedat": i["publishedAt"]
            })

        return JsonResponse(context)
    except Exception as e:
        return JsonResponse({"success": False})
