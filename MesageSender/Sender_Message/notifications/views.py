from django.shortcuts import render, redirect


from django.contrib.auth.models import User  # Assuming you have User model

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def notify_user(user, message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'user_{user.id}',  # Send to the specific user's group
        {
            'type': 'send_message',
            'message': message,
        }
    )


def notification_view(request):
    return render(request, 'notifications.html')


def send_notification_view(request):
    if request.method == 'POST':
        # Assuming you're sending the notification to the logged-in user
        user = request.user  
        message = "This is your notification message!"
        notify_user(user, message)
        return redirect('send_notification')  # Redirect to the notification view

    return render(request, 'send_notification.html')  # In case you need to display the form/page
