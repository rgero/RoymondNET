from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    # Need an automated slug.


class Post(models.Model):
    post_title = models.CharField(max_length=200, help_text="This is the title of the project")
    content = models.TextField(help_text="Markdown Enabled.")
    author = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    categories = models.ManyToManyField("Category", blank=True)

    def __str__(self):
        return self.post_title

    def publish(self):
        self.published_date = timezone.now()
        self.save()
