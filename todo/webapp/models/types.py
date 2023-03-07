
from django.db import models

class Type(models.Model):
    TYPE_CHOICES = (
        ('Task', 'задача'),
        ('Bug', 'ошибка'),
        ('Enhancement', 'улучшение')
    )
    name = models.CharField(max_length=255, verbose_name='название',choices= TYPE_CHOICES,null=False, blank=False )

    def __str__(self):
        return f'{self.name}'