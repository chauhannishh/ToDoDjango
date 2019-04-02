from django.db import models

class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=200)
    desc = models.TextField(max_length=200)
    schedule_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(blank=True,null=True)

    def __str__(self):
        return self.title
