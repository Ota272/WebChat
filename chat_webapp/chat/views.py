from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import User, Message
from .forms import UserForm, MessageForm

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['user_id'] = user.id
            return redirect('chat')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

def chat(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect('register')
    
    user = get_object_or_404(User, id=user_id)
    messages = Message.objects.filter(archived=False).order_by('-timestamp')
    archived_messages = Message.objects.filter(user=user, archived=True).order_by('-timestamp')

    if request.method == 'POST':
        if 'edit_message_id' in request.POST:
            message_id = request.POST.get('edit_message_id')
            message = get_object_or_404(Message, id=message_id, user=user)
            form = MessageForm(request.POST, instance=message)
            if form.is_valid():
                form.save()
                messages.success(request, 'Message updated successfully.')
                return redirect('chat')
            else:
                messages.error(request, 'Failed to update message. Please check the form.')
        elif 'delete_message_id' in request.POST:
            # archive instead of deleting permanently
            message_id = request.POST.get('delete_message_id')
            message = get_object_or_404(Message, id=message_id, user=user)
            message.archived = True
            message.save()
            messages.success(request, 'Message archived.')
            return redirect('chat')
        elif 'restore_message_id' in request.POST:
            message_id = request.POST.get('restore_message_id')
            message = get_object_or_404(Message, id=message_id, user=user, archived=True)
            message.archived = False
            message.save()
            messages.success(request, 'Message restored.')
            return redirect('chat')
        else:
            form = MessageForm(request.POST)
            if form.is_valid():
                new_message = form.save(commit=False)
                new_message.user = user
                new_message.save()
                messages.success(request, 'Message sent.')
                return redirect('chat')
            else:
                messages.error(request, 'Failed to send message. Please check the form.')
    else:
        form = MessageForm()
    return render(request, 'chat.html', {
        'user': user,
        'messages': messages,
        'archived_messages': archived_messages,
        'form': form
    })