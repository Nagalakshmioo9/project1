from django.contrib import admin 
from django.urls import path 
from .views import index,logout 
from admins.views import  
adminlogin,adminlogincheck,activateusers,activatewaitedusers,viewresults 
from users.views import  
userlogin,userregister,userRegisterAction,userlogincheck,userwritestatements,userstatementrecor d 
from django.conf import settings 
from django.conf.urls.static import static 
urlpatterns = [ 
 path('admin/', admin.site.urls), 
 path('',index,name='index'), 
 path('logout',logout,name='logout'), 
 path('adminlogin',adminlogin,name='logout'),
 path('adminlogin',adminlogin,name='adminlogin'), 
 path('adminlogincheck',adminlogincheck,name='adminlogincheck'), 
 path('activateusers',activateusers,name='activateusers'), 
 path('activatewaitedusers',activatewaitedusers,name='activatewaitedusers'),  path('viewresults',viewresults,name='viewresults'), 
 path('userRegisterAction',userRegisterAction,name='userRegisterAction'),  
path('userlogin',userlogin,name='userlogin'), 
 path('userregister',userregister,name='userregister'), 
 path('userlogincheck',userlogincheck,name='userlogincheck'), 
 path('userwritestatements',userwritestatements,name='userwritestatements'), 
 path('userstatementrecord',userstatementrecord,name='userstatementrecord'), if settings.DEBUG: 
 urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
