from django.shortcuts import render
from .models import Issue
# Create your views here.


def index(request):

    num_issues = Issue.objects.all().count()
    open_issues = Issue.objects.filter(status__in=["New", "On Hold", "Waiting"])

    context = {
        "num_issues" : num_issues,
        "open_issues" : open_issues,
    }

    return render(request, 'index.html', context=context)