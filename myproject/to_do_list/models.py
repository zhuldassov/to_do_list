from django.db import models

class Task(models.Model):
    STATUS_CHOICES = (
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('done', 'Сделано'),
    )

    title = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата')

    def __str__(self):
        return self.title
