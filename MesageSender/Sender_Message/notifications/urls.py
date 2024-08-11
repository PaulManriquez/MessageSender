from django.urls import path
from . import views

urlpatterns = [
    path('notifications/', views.notification_view, name='notifications'),
    path('send-notification/', views.send_notification_view, name='send_notification'),
]
