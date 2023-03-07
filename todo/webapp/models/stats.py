from django.db import models


class Status(models.Model):
    STATUS_CHOICES = (
            ('new', 'New'),
            ('in_progress', 'In Progress'),
            ('done', 'Done')
        )
    name = models.CharField(max_length=255, verbose_name='название',choices= STATUS_CHOICES, null=False, blank=False )


    def __str__(self):
        return f'{self.name}'