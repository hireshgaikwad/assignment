from django.urls import path
from . import views

urlpatterns = [
    path("",views.Indexpage,name="index"),
    path("signup/",views.Signuppage,name="signup"),
    path("register/",views.Register,name="register"),
    path("loginpage/",views.Loginpage,name="loginpage"),
    path("login/",views.LoginUser,name="login"),
    path("profile/<int:pk>",views.ProfilePage,name="profile"),
    path("home/",views.Homepage,name="home"),
    path("createpage/",views.Createpage,name="createpage"),
    path("create/<int:pk>",views.Create,name="create"),
    path("poll/",views.POllpage,name="poll"),
    path("vote/<int:pk>",views.Vote,name="vote"),
    path('results/<int:pk>/',views.results, name='results'),
    path("logout/",views.logout,name="logout"),

    
]
