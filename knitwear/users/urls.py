from django.urls import path
from users.views import LoginUser, logout_user, RegisterUser, ProfileUser

app_name = 'users'

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('profile/', ProfileUser.as_view(), name='profile'),
    path('logout/', logout_user, name='logout'),
]
