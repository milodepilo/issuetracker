from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Comment(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    comment_body = models.TextField("Text")
    created_by = models.OneToOneField(User, on_delete="DO_NOTHING")


# Create your models here.
class Issue(models.Model):
    PRIORITY_CRIT = "P1"
    PRIORITY_HIGH = "P2"
    PRIORITY_LOW = "P3"
    PRIORITY_CHOICES = [
        (PRIORITY_CRIT, "Critical"),
        (PRIORITY_HIGH, "High"),
        (PRIORITY_LOW, "Low"),
    ]
    STATUS_NEW = "New"
    STATUS_ON_HOLD = "On Hold"
    STATUS_WAITING = "Waiting"
    STATUS_CANCELED = "Canceled"
    STATUS_RESOLVED = "Resolved"
    STATUS_CHOICES = [
        (STATUS_NEW, "New"),
        (STATUS_ON_HOLD, "On Hold"),
        (STATUS_WAITING, "Waiting"),
        (STATUS_CANCELED, "Canceled"),
        (STATUS_RESOLVED, "Resolved"),
    ]
    brief_description = models.TextField("Summary")
    description = models.TextField()
    priority = models.CharField(
        max_length=2, choices=PRIORITY_CHOICES, default=PRIORITY_LOW
    )
    status = models.TextField(choices=STATUS_CHOICES, default=STATUS_NEW)
    # added_files = models.FileField(
    #     "files",
    #     null=True,
    # )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete="DO_NOTHING")
    # updated_by = models.CharField(max_length=70)
    # assigned_to = models.CharField(max_length=70)

    def __str__(self):
        return self.brief_description

