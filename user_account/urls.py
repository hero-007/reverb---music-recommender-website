from django.urls import path,include
from . import views

# list of urls associated with the application
urlpatterns=[
    path('',views.index,name='index'),
    path('register_user',views.load_register_page,name='load_register_page'),
    path('register_here',views.register_here,name='register_here'),
    path('login_user',views.load_login_page,name='load_login_page'),
    path('login_here',views.login_here,name='login_here'),
    path('logout_here',views.logout_here,name='logout_here'),
    path('recommend_here',views.recommend_here,name='recommend_here'),
]