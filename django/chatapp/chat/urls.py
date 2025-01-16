from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView  # Import LogoutView

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('login/', views.login_view, name='login'),  # Login page
    path('signup/', views.signup_view, name='signup'),  # Sign-up page
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user-list/', views.user_list_view, name='user_list'),
    path('', views.user_list, name='user_list'),  # List of users to chat with
    path('chat/<int:user_id>/', views.chat_room, name='chat_room'),
]
