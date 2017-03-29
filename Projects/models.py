from django.db import models

# Create your models here.
class Language(models.Model):
    language = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.language


class ProjectPage(models.Model):
    pageTitle = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    language = models.ForeignKey(Language)
    # Still need quick facts.
    content = models.TextField()
    images = models.TextField(null=True, blank=True)
    related_projects = models.ManyToManyField("self", blank=True, symmetrical=False)

    def __str__(self):
        return self.pageTitle
