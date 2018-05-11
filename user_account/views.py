from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Listener,User_Id
from django.contrib.auth import authenticate,login,logout
from . import basic
from . import music

# Create your views here.
def index(request):
    context = {'username':None,'login_status':False,'songs':None,}
    if request.user.is_authenticated:
        context['username'] = request.user
        context['login_status'] = True
        song_list = basic.give_me_song_list(request.user)
        context['songs'] = song_list
    return render(request,'user_account/index.html',context)

def load_register_page(request):
    return render(request,'user_account/register_page.html',{})

def register_here(request):
    context = {'response':'new user has been registered successfully'}
    try:
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        name = request.POST["name"]
    except KeyError:
        context['response']='Something went wrong try again !!'
        return render(request,'user_account/response.html',context)

    user = User.objects.create_user(username,email,password)
    user.save()
    user_temp_id = user.pk
    sample_user = User_Id.objects.get(pk=user_temp_id)
    sample_user_id = sample_user.user_id
    listener = Listener(listener_id = sample_user_id,listener_name = name)
    listener.listener_save()
    return render(request,'user_account/response.html',context)

def load_login_page(request):
    return render(request,'user_account/login.html',{})

def login_here(request):
    context = {}
    try:
        username = request.POST["username"]
        password = request.POST["password"]
    except KeyError:
        return HttpResponse('You are doing something wrong ')
    user_hello = authenticate(request,username=username, password=password)
    if user_hello is not None:
        login(request,user_hello)
        context['response']='{} is logged in successfully'.format(username)
        return render(request,'user_account/response.html',context)
    else:
        context['response']='Please Enter the correct credentials'
        return render(request,'user_account/response.html',context)

def logout_here(request):
    current_user = request.user
    logout(request)
    context = {'response':'You are logged out successfully'}
    return render(request,'user_account/response.html',context)

def recommend_here(request):
    context ={'recommended_songs':None}
    current_user = request.user
    dummy_user = Listener.objects.get(listener_name = current_user)
    dummy_user_id = dummy_user.listener_id
    input_id = User_Id.objects.get(user_id = dummy_user_id)
    index_to_pass = input_id.user_index
    recommended_songs = music.give_recommended_songs(index_to_pass)
    context['recommended_songs']=recommended_songs
    return render(request,'user_account/recommended.html',context)




