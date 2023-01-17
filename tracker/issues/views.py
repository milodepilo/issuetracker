from django.shortcuts import render
from .models import Issue, Comment
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

# Create your views here.


def index(request):
  num_issues = Issue.objects.all().count()
  open_issues = Issue.objects.filter(
    status__in=["New", "On Hold", "Waiting"]).count()

  context = {
    "num_issues": num_issues,
    "open_issues": open_issues,
  }

  return render(request, 'index.html', context=context)


class IssueListView(generic.ListView):
  model = Issue
  context_object_name = 'issue_list'
  queryset = Issue.objects.all().order_by("priority")
  paginate_by = 10


class IssueDetailView(generic.DetailView):
  model = Issue


class CommentDetailView(generic.DetailView):
  model = Comment


class OpenIssueListView(generic.ListView):
  model = Issue
  context_object_name = "open_issue_list"
  template_name = "issues/open_issue_list.html"
  queryset = Issue.objects.filter(status__in=["New", "On Hold", "Waiting"])
  paginate_by = 10


class IssueCreateView(CreateView):
  model = Issue


class IssueUpdateView(UpdateView):
  model = Issue


class IssueDeleteView(DeleteView):
  model = Issue
