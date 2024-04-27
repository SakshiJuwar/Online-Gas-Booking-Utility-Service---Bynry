from gasutilityapp import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
#from django.contrib import admin

urlpatterns = [
    #path('admin/',admin.site.urls),
    path('home',views.home),
    path('logout',views.user_logout),
    path('register',views.register),
    path('login',views.user_login),
    path('connection',views.connection),
    #path('cylinder',views.cylinder),
    path('viewconnection',views.viewconnection),
    path('delete/<rid>',views.deleteconnection),
    path('edit/<rid>',views.editconnection),
    path('booking/<rid>',views.booking),
    path('viewbooking',views.viewbooking),
    path('deletebooking/<rid>',views.deletebooking),
]