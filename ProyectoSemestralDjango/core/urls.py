from django.urls import path
from .views import AboutUs, Login, Register, index, news

urlpatterns = [
    path('',index,name="index"),
    path('AboutUs/',AboutUs, name="AboutUs"),
    path('Login/', Login, name="Login"),
    path('news/', news, name="news"),
    path('Register/', Register, name="Register"),

    
]