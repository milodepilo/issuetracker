from django.db import models
from authentication.models import User
from django.urls import reverse


class Comment(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    comment_body = models.TextField("Text", unique=False)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, unique=False)
    related_issue = models.ForeignKey('issue', on_delete=models.CASCADE, default="")
    added_files = models.FileField("files", null=True, blank=True)


    def __str__(self):
        return f"issue{self.id}"


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
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="creator", default="")
    assigned_to = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="Assignee", default="", null=True)
    # updated_by = models.CharField(max_length=70)

    # added_files = models.FileField(
    #     "files",
    #     null=True,
    # )

    class Meta:
        ordering = ['-date_created']

    def get_absolute_url(self):
        return reverse('issue-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.brief_description
