from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),  # Include the chat app's URLs
    path('chat/', include('chat.urls')),  # Include the chat app's URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Login, logout URLs
]
