from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.chat_home, name='chat_home'),  # Make chat_home the default route
    path('chat/<int:user_id>/', views.chat_with_user, name='chat_with_user'),  # Chat with specific user
]
