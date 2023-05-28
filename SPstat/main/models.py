from django.db import models

class Price(models.Model):
    server_title = models.CharField('new server name', max_length=50)
    price = models.TextField('hash')

    def __str__(self):
        return self.server_title

    class Meta:
        verbose_name = 'server'
        verbose_name_plural = 'servers'