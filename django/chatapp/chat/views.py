from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Message, ChatRoom
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


def home(request):
    return render(request, 'chat/home.html')  # Update with the correct template path

def signup(request):
    return render(request, 'chat/signup.html')  # Update with the correct template path


def login_view(request):
    return render(request, 'chat/login.html')  # Adjust template path as needed

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            login(request, user)  # Log the user in automatically after registration
            messages.success(request, 'Registration successful!')
            return redirect('home')  # Redirect to the home page after registration
        else:
            messages.error(request, 'Error during registration. Please try again.')
    else:
        form = UserCreationForm()
    return render(request, 'chat/signup.html', {'form': form})

def user_list_view(request):
    users = User.objects.all()  # Fetch all users
    return render(request, 'user_list.html', {'users': users})

def user_list(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/user_list.html', {'users': users})

@login_required
def chat_room(request, user_id):
    # Check if a chat room exists between the logged-in user and the other user
    user = User.objects.get(id=user_id)
    room, created = ChatRoom.objects.get_or_create(
        user1=request.user, user2=user
    )
    if created:  # If the chat room was just created
        room, created = ChatRoom.objects.get_or_create(
            user1=user, user2=request.user
        )

    # Get all messages in the chat room
    messages = Message.objects.filter(room=room).order_by('timestamp')

    if request.method == 'POST':
        message_content = request.POST.get('message')
        if message_content:
            Message.objects.create(
                room=room,
                sender=request.user,
                content=message_content
            )
            return redirect('chat_room', user_id=user.id)

    return render(request, 'chat/chat_room.html', {'room': room, 'messages': messages, 'user': user})