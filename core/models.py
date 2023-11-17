from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords



class Application(models.Model):
    date = models.DateTimeField(default=timezone.now, verbose_name = 'Дата и Время')
    auth_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name = 'Преподователь')
    description = models.TextField('Описание проблемы')

    class Meta:
        #managed = False
        db_table = 'applications'
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'№{self.id} Заявитель {self.auth_user}'