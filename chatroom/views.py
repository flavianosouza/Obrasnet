from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from . models import Chatroom
from core.models import Expert

expert_positions = [
    'administrator',
    'consultora',
    'contratante',
    'trabalhadora'
]

# Chatting page for consulting experts and clients
## Expert List Page
@login_required
def expert_list(request):
    experts = Expert.objects.all()

    return render(request, 'expert_list.html', { 'experts': experts, 'positions': expert_positions })

## Expert Chat Room
@login_required
def expert_chat(request, expert_id, user_id):

    expert = Expert.objects.get(id=expert_id)
    
    return render(request, 'expert_chat.html', { 'expert': expert })

# Chatting page for users
@login_required
def user_chat(request):
    rooms = Chatroom.objects.all()

    return render(request, 'user_chat.html', { 'rooms': rooms })

