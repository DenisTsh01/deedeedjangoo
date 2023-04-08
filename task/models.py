from django.db import models
from users.models import ExtendUser
from django.utils import timezone


class TaskCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


task_status = (
    ('Done', 'Done'),
    ('Uncompleted', 'Uncompleted'),
    ('Remove', 'Remove'),

)


class Task(models.Model):
    task_name = models.CharField(max_length=50)
    task_date = models.DateTimeField(default=timezone.now(), null=False)
    task_deadline = models.DateTimeField(default=timezone.now(), null=False)
    task_information = models.CharField(max_length=50, null=False)
    days_until_deadline = models.IntegerField(default=0, null=False)
    extend_user = models.ForeignKey(ExtendUser, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE)
    completed = models.CharField(max_length=50,default='Uncompleted', choices=task_status, null=False)
    # stat_hour = models.TimeField(null=False)

    def __str__(self):
        return self.category

