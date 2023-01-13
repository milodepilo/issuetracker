# Generated by Django 4.1.5 on 2023-01-13 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Issue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("brief_description", models.TextField(verbose_name="Summary")),
                ("description", models.TextField()),
                (
                    "priority",
                    models.CharField(
                        choices=[("P1", "Critical"), ("P2", "High"), ("P3", "Low")],
                        default="P3",
                        max_length=2,
                    ),
                ),
                (
                    "status",
                    models.TextField(
                        choices=[
                            ("New", "New"),
                            ("On Hold", "On Hold"),
                            ("Waiting", "Waiting"),
                            ("Canceled", "Canceled"),
                            ("Resolved", "Resolved"),
                        ],
                        default="New",
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-date_created"],
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
                ("comment_body", models.TextField(verbose_name="Text")),
                (
                    "created_by",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
