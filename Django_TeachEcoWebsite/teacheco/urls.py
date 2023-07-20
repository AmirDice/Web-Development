"""teacheco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from personal.views import *
from members.views import *
from members.urls import *
from django.contrib.auth import views as auth_views
from personal.views import loadcontent
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('admin/', admin.site.urls),
    path('home', home_view, name="home"),
    path('accounts/', include('allauth.urls')),
    # path('signup', signup_view),
    path('', landing_view),
    path('blog', BlogView.as_view(), name="blog"),
    path('blogsingle/<int:pk>', BlogSingle.as_view(), name='blog-single'),
    path('contact', contact_view),
    path('addpost', AddPostView.as_view(), name='addpost'),
    path('blogsingle/edit/<int:pk>', UpdatePostView.as_view(), name='updatepost'),
    path('blogsingle/<int:pk>/delete',
         DeletePostView.as_view(), name='deletepost'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('editprofile/', UserEditView.as_view(), name='editprofile'),
    path('blogsingle/<int:pk>/comment/',
         AddCommentView.as_view(), name='add_comment'),
    path('next', views.loadcontent, name="Loadcontent"),
    path('singlechallenge/', singlechallenge, name='singlechallenege'),
    # path('image_upload', singlechallenge, name = 'image_upload'),
    path('success/', success, name='success'),
    path('uploadedimages/', display_uploaded_images, name='uploadedimages'),
    path('quizes/', include('quizes.urls')),


]

(r'(?:.*?/)?(?P(Vendors|Jquery|Js|media)/.+)$',
 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
