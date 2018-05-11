from django.contrib import admin
from .models import Listener,User_Id,Song
# Register your models here.
admin.site.register(Listener)
admin.site.register(User_Id)
admin.site.register(Song)