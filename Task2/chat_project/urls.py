from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('chat.urls')),  # Includes the URLs of the chat app
]
