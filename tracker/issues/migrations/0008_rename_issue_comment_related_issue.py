# Generated by Django 4.1.5 on 2023-01-13 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("issues", "0007_alter_comment_added_files"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="issue",
            new_name="related_issue",
        ),
    ]
