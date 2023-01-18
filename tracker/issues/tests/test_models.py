from django.test import TestCase
from .models import Issue


class IssueModelTest(TestCase):

  @classmethod
  def setUpTestData(cls):
    Issue.objects.create(brief_description="test issue",
                         description="this is a test isue")

  def status_for_new_issue_is_new(self):
    issue = Issue.objects.get(id=1)
    status = issue._meta.get_field('status')
    self.assertEqual(status, "new")