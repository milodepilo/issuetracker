from django.shortcuts import render, get_object_or_404
from .models import Issue, Comment
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddCommentForm
from django.urls import reverse
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


class IssueDetailView(FormMixin, generic.DetailView):
    model = Issue
    form_class = AddCommentForm

    def get_success_url(self):
        return reverse("issue-detail-view", kwargs={"pk": self.object.pk})
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment_instance = form.save(commit=False)
            comment_instance.created_by = request.user
            comment_instance.related_issue = self.object
            comment_instance.save()
            self.object.comment_set.add(comment_instance)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_comment_form"] = AddCommentForm()
        return context


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


