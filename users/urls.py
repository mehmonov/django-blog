
from django.urls import path

from .views import login_profile, user_logout, profile, user_sign

urlpatterns = [
    path('login/', login_profile, name='login_profile'),
    path('user_sign/', user_sign, name='user_sign'),
    path('profile/', profile, name='profile'),
    
    path('user_logout/', user_logout, name='user_logout'),
    

]  
