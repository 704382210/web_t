from django.contrib import admin
from django.conf.urls import *
from views.userViews import index,register,userList
urlpatterns = [
    url('admin/', admin.site.urls),
    url('^index/$',index),
    url('^register/$',register),
    url('^userList/$',userList),
]
