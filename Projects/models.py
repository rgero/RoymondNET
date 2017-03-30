from django.db import models

# Create your models here.
class Language(models.Model):
    language = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.language


class ProjectPage(models.Model):
    pageTitle = models.CharField(max_length=200, help_text="This is the title of the project")
    slug = models.SlugField(max_length=200, unique=True)
    language = models.ForeignKey(Language)
    quick_facts = models.TextField(null=True, blank=True, help_text="HTML Enabled.")
    content = models.TextField(help_text="Markdown Enabled.")
    images = models.TextField(null=True, blank=True, help_text="Just the name and extension. The files must be in the correct static directory!")
    external_media = models.TextField(null=True, blank=True, help_text="HTML Enabled")
    related_projects = models.ManyToManyField("self", blank=True, symmetrical=False)

    def __str__(self):
        return self.pageTitle
