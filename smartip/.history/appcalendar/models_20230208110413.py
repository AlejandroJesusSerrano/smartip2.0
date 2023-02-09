from django.db import models
from appsmartip.models import Pendings

# Create your models here.
class PendinfCalendar(models.Model):
    date = models.ForeignKey(Pendings, related_name='date', on_delete=models.CASCADE)
    person = models.ForeignKey(Pendings, related_name='service_for', on_delete=models.CASCADE)
    office = models.ForeignKey(Pendings, related_name='office', on_delete=models.CASCADE)
    device = models.ForeignKey(Pendings, related_name='device', on_delete=models.CASCADE)
    task = models.ForeignKey(Pendings, related_name='reason', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.task
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'tasks'
        ordering = ['-date']

