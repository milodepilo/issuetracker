from django.contrib import admin
from .models import Comment, Issue
from authentication.models import User
# Register your models here.


class CommentsInline(admin.StackedInline):
    model = Comment


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ("id", "priority", "brief_description", "date_created", "created_by")
    list_filter = ("priority",)
    inlines = [CommentsInline]
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display =("id", "related_issue", "created_by", "date_created")

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

