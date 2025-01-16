import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Message
from django.db.models import Q
from django.contrib.auth.models import User


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('chat_home')
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # Redirect to the page the user was trying to access before login
            next_page = request.GET.get('next', 'chat_home')  # Default to 'chat_home' if no 'next' parameter
            return redirect(next_page)
        return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def chat_home(request):
    users = User.objects.exclude(id=request.user.id)

    # Add the last message for each user
    for user in users:
        last_message = Message.objects.filter(
            Q(sender=request.user, recipient=user) | Q(sender=user, recipient=request.user)
        ).order_by('-id').first()
        if last_message:
            try:
                last_message_content = json.loads(last_message.content).get("message", "No messages yet.")
            except (json.JSONDecodeError, KeyError):
                last_message_content = "No messages yet."
        else:
            last_message_content = "No messages yet."
        
        # Attach the last message to the user object
        user.last_message = last_message_content

    return render(request, 'chat_home.html', {'users': users})


def chat_with_user(request, user_id):
    recipient = User.objects.get(id=user_id)
    messages = Message.objects.filter(
        sender=request.user, recipient=recipient
    ) | Message.objects.filter(
        sender=recipient, recipient=request.user
    )

    # Extract only the message text from JSON content
    parsed_messages = []
    for msg in messages:
        try:
            content = json.loads(msg.content).get("message", "No message content")
            parsed_messages.append({'sender': msg.sender, 'content': content})
        except (json.JSONDecodeError, KeyError):
            parsed_messages.append({'sender': msg.sender, 'content': "No message content"})

    if request.method == 'POST':
        content = request.POST['content']
        Message.objects.create(sender=request.user, recipient=recipient, content=json.dumps({"message": content}))
        return redirect('chat_with_user', user_id=user_id)

    return render(request, 'chat.html', {'recipient': recipient, 'messages': parsed_messages})
