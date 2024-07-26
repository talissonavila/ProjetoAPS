# Generated by Django 4.2.14 on 2024-07-24 13:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("theblog", "0004_category_post_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
        migrations.AddField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(related_name="blog_posts", to=settings.AUTH_USER_MODEL),
        ),
    ]
