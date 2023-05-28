from django.db import models

class Price(models.Model):
    server_title = models.CharField('как азим звал', max_length=50)
    price = models.TextField('количетсво')

    def __str__(self):
        return self.server_title

    class Meta:
        verbose_name = 'kek'
        verbose_name_plural = 'keks'