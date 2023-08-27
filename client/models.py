from django.db import models

NULLABLE = {'null': True, 'blank': True}


class MailingClient(models.Model):

    contact_email = models.EmailField(max_length=254, unique=True, verbose_name='контактный email')
    first_name = models.CharField(max_length=25, verbose_name='имя')
    last_name = models.CharField(max_length=25, verbose_name='фамилия')
    surname = models.CharField(max_length=25, verbose_name='отчество', **NULLABLE)
    comment = models.TextField(verbose_name='комментарии', **NULLABLE)

    def __str__(self):
        return f'Получатель {self.first_name} {self.last_name} {self.contact_email}'

    class Meta:
        verbose_name = "Клиент рассылки"
        verbose_name_plural = 'Клиенты рассылок'