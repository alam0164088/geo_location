# geo_project/geo_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # আমাদের ট্র্যাকিং পেজ
    path('', include('tracking.urls')),
    
    # Django এর ডিফল্ট লগইন/লগআউট (যাতে /accounts/login/ কাজ করে)
    path('accounts/login/', auth_views.LoginView.as_view(template_name='tracking/location.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # যদি কেউ রুটে আসে তাহলে সরাসরি লোকেশন পেজে নিয়ে যাক
    path('', RedirectView.as_view(url='/location/', permanent=False)),
]