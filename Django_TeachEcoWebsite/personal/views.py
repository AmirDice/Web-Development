from django.db.models import fields
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls.base import reverse_lazy
from members.forms import CommentForm, EditProfileForm
from personal.models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import EditForm, PostForm, ImageForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views import generic
from django.shortcuts import get_object_or_404
import requests
from teacheco import settings
from django.shortcuts import render, redirect
from .models import Image
# Create your views here.


def landing_view(request):
    return render(request, "landingpage.html", {})


# https: // newsapi.org/v2/everything?q = apple & from = 2021-11-23 & to = 2021-11-23 & sortBy = popularity & apiKey = f90db0776ba540dc8ee7bd468d5f45c0


def home_view(request):
    import json

    page = request.GET.get('page', 1)
    search = request.GET.get('search', None)

    if search is None or search == "top":
        # get the top news
        url = "https://newsapi.org/v2/everything?q=eco-friendly&apiKey=f90db0776ba540dc8ee7bd468d5f45c0".format(
            "us", 1, settings.APIKEY
        )
    else:
        # get the search query request
        url = "https://newsapi.org/v2/everything?q=eco-friendly&apiKey=f90db0776ba540dc8ee7bd468d5f45c0".format(
            search, "popularity", page, settings.APIKEY
        )
    r = requests.get(url=url)

    data = r.json()
    if data["status"] != "ok":
        return HttpResponse("<h1>Request Failed</h1>")
    data = data["articles"]
    context = {
        "success": True,
        "data": [],
        "search": search
    }
    # seprating the necessary data
    for i in data:
        context["data"].append({
            "title": i["title"],
            "description":  "" if i["description"] is None else i["description"],
            "url": i["url"],
            "image": temp_img if i["urlToImage"] is None else i["urlToImage"],
            "publishedat": i["publishedAt"]
        })
    # send the news feed to template in context
    return render(request, 'index.htm', context=context)


def loadcontent(request):
    try:
        page = request.GET.get('page', 1)
        search = request.GET.get('search', None)
        # url = "https://newsapi.org/v2/everything?q={}&sortBy={}&page={}&apiKey={}".format(
        #     "Technology","popularity",page,settings.APIKEY
        # )
        if search is None or search == "top":
            url = "https://newsapi.org/v2/everything?q=eco-friendly&apiKey=f90db0776ba540dc8ee7bd468d5f45c0".format(
                "us", page, settings.APIKEY
            )
        else:
            url = "https://newsapi.org/v2/everything?q=eco-friendly&apiKey=f90db0776ba540dc8ee7bd468d5f45c0".format(
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

    # posts = Post.objects.all()
    # return render(request, "index.htm", {'posts': posts})


# def signup_view(request):
 #   print(request.headers)
  #  return render(request, "signup.htm")


# def blog_view(request):
 #   posts = Post.objects.all()
  #  return render(request, "blog.html", {'posts': posts})

class BlogView(ListView):
    model = Post
    template_name = 'blog.html'


def show_challenge(request):
    return render(request, "Challenge.html", {})


def show_elearning(request):
    return render(request, "E-learning.html", {})


# def quiz_view(request):
#     return render(request, "Quizzes.html", {})


def contact_view(request):
    return render(request, "Contact.html", {})


# def blog_single_view(request):
   # posts = Post.objects.all()
   # return render(request, "Blog-Single.html", {'posts': posts})

class BlogSingle(DetailView):
    model = Post
    template_name = 'Blog-Single.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     pk = self.kwargs["pk"]
    #     #slug = self.kwargs["slug"]

    #     form = CommentForm()
    #     post = get_object_or_404(Post, pk=pk)
    #     comments = post.comment_set.all()

    #     context['post'] = post
    #     context['comments'] = comments
    #     context['form'] = form
    #     return context

    # def post(self, request, *args, **kwargs):
    #     form = CommentForm(request.POST)
    #     self.object = self.get_object()
    #     context = super().get_context_data(**kwargs)

    #     post = Post.objects.filter(id=self.kwargs['pk'])[0]
    #     comments = post.comment_set.all()

    #     context['post'] = post
    #     context['comments'] = comments
    #     context['form'] = form

    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         email = form.cleaned_data['email']
    #         body = form.cleaned_data['body']

    #         comment = Comment.objects.create(
    #             name=name, email=email, body=body, post=post
    #         )

    #         form = CommentForm()
    #         context['form'] = form
    #         return self.render_to_response(context=context)

    #     return self.render_to_response(context=context)
    # form = CommentForm

    # def post(self, request, *args, **kwargs):
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         post = self.get_object()
    #         form.instance.user = request.user
    #         form.instance.post = post
    #         form.save()

    #         return redirect(reverse)


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addpost.html'
    #fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'updatepost.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'deletepost.html'
    success_url = reverse_lazy('blog')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'editprofile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments.html'
    #fields = '__all__'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('blog')


def success(request):
    return render(request, 'popup.html')


def singlechallenge(request):

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'SingleChallenge.html', {'form': form})


def display_uploaded_images(request):

    if request.method == 'GET':

        # getting all the objects of hotel.
        Images = Image.objects.all()
        return render((request, 'SingleChallenge.html',
                       {'upload_images': Images}))
