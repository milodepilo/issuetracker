from django.shortcuts import render, get_object_or_404
from .models import Issue, Comment
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def index(request):
    num_issues = Issue.objects.all().count()
    open_issues = Issue.objects.filter(status__in=["New", "On Hold", "Waiting"]).count()

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


class PersonalizedIssueListView(generic.ListView):
    model = Issue
    context_object_name = "personalized_issue_list"
    template_name = "issues/personalized-issue-list.html"

    def get(self, request, *args, **kwargs):
        ...


class IssueCreateView(LoginRequiredMixin, CreateView):
  model = Issue
  fields = ["brief_description", "description", "priority", "assigned_to"]

  def form_valid(self, form):
      form.instance.created_by = self.request.user
      return super().form_valid(form)


class IssueUpdateView(UpdateView):
  model = Issue
  fields = [
    "brief_description", "description", "priority", "status", "assigned_to",
  ]


class IssueDeleteView(DeleteView):
  model = Issue


