from django.db import models
from django.utils import timezone

class Message(models.Model):
    address = models.EmailField("Адресат")
    message = models.TextField("Сообщение")
    sending_delay = models.PositiveIntegerField("Задержка отправки письма (секунды)", default=0)
    created = models.DateTimeField("Время создания", auto_now_add=True)
    status = models.CharField("Статус", max_length=10, default="Не отправлено")

    def __str__(self):
        return "{} {}".format(self.address, self.message)

    class Meta:
        verbose_name = "Письмо"
        verbose_name_plural = "Письма"