from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()
    done_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Task, self).save(*args, **kwargs)

    class Meta:
        db_table="task"