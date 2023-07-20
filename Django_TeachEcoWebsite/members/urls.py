from django.urls import path
from members import views
from django.urls import path
from members import views as members_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    #     path('login/', views.loginPage, name="login"),
    #     path('logout/', views.logoutUser, name="logout"),
    path('next', views.loadcontent, name="Loadcontent"),
]
