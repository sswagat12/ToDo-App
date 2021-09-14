from django.contrib.auth.models import User
from django.db import models

"""Contact Us Model"""


class ContactUs(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=10)
    queryIfAny = models.CharField(max_length=120)
    date = models.DateTimeField()

    def __str__(self):
        return self.name


""""""
class ToDo(models.Model):
    title = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    status_choices = [('COMPLETED', 'COMPLETED'),
                        ('PENDING', 'PENDING') ]
    status = models.CharField(max_length=10, choices= status_choices)
    date = models.DateTimeField(auto_now_add=True)
    priority_choices = [('HIGH', 'HIGH'),
                        ('LOW', 'LOW'),
                        ('MEDIUM', 'MEDIUM')]
    priority = models.CharField(max_length=10, choices=priority_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
