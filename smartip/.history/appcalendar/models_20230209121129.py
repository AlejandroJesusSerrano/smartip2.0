from django.db import models
from appsmartip.models import *

# Create your models here.

class CalendarPendings(models.Model):
    date_in = models.ForeignKey(Pendings, on_delete=models.CASCADE)
    service_for = models.ForeignKey(DevUsers, related_name='service_for', on_delete=models.CASCADE)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    reason = RichTextField()
    state = models.ForeignKey(PendingStatus, default=1, on_delete=models.CASCADE)
    updated = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return self.task
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['-date_in']