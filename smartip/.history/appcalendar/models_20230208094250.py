from django.db import models
from ckeditor.fields import RichTextField
from appsmartip.models import DevUsers, Office, Device, PendingStatus

# Create your models here.
class Pendings(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    required_by = models.ForeignKey(DevUsers, related_name='user_require', on_delete=models.CASCADE)
    personal = models.BooleanField()
    service_for = models.ForeignKey(DevUsers, related_name='user_for', on_delete=models.CASCADE)
    office = models.ForeignKey(Office, related_name='office_name', on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    reason = RichTextField()
    state = models.ForeignKey(PendingStatus, default=1, on_delete=models.CASCADE)
    updated = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.task
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['-date']

