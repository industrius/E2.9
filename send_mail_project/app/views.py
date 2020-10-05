from django.shortcuts import render, HttpResponseRedirect
from .models import Message
from django.conf import settings
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from .forms import MessageForm
import threading
import time
from django.core.mail import send_mail


class MessageListView(ListView):
    model = Message
    template_name = "list.html"
    def get_queryset(self):
        return Message.objects.order_by("created").reverse()[:10]


class MessageView(FormView):
    form_class = MessageForm
    template_name = "index.html"
    success_url = "/list"
    def form_valid(self, form):
        form.save()
        ThredManager()
        return super(MessageView, self).form_valid(form)


def ThredManager():
    """
    Функция проверки неотправленных сообщений в БД
    и запуска потоков для их отправки
    """
    messages = Message.objects.filter(status = "Не отправлено")
    threads = []
    for message in messages:
        kw = {
            "message_id":message.id,
            "address":message.address,
            "message":message.message,
            "sending_delay":message.sending_delay,
        }
        thread = threading.Thread(target=SendMail, kwargs=kw)
        threads.append(thread)
        thread.start()
        message.status = "Отправка через {} сек.".format(message.sending_delay)
        message.save()
    return HttpResponseRedirect("/list")


def SendMail(message_id, address, message, sending_delay):
    """
    Функция отправки сообщения и 
    обновления статуса сообщения
    """
    time.sleep(sending_delay)
    result = send_mail("SkillFactory: E2.9 Домашнее задание", message, "industrius.d@gmail.com", (address,), fail_silently=True)
    message = Message.objects.filter(id=message_id).first()
    if result == 1:
        message.status = "Отправлено"
    else:
        message.status = "Ошибка"
    message.save()