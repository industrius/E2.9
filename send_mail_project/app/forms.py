from django import forms
from .models import Message
from django.conf import settings
from django.core.mail import send_mail


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        exclude = ("success", "status",)