from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name='index'),
  path('list/', views.IssueListView.as_view(), name='list'),
  path("open_issue/", views.OpenIssueListView.as_view(), name="open-issues"),
  path('issue/<int:pk>',
       views.IssueDetailView.as_view(),
       name='issue-detail-view'),
  path('comment/<int:pk>',
       views.CommentDetailView.as_view(),
       name='comment-detail-view'),
  path("create/", views.IssueCreateView.as_view(), name="issue-create-view"),
  path("issue/<int:pk>/update",
       views.IssueUpdateView.as_view(),
       name="issue-update-view"),
  path("issue/<int:pk>/delete",
       views.IssueDeleteView.as_view(),
       name="issue-delete-view")
]
