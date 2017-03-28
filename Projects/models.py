from django.db import models

# Create your models here.
class Language(models.Model):
    language = models.CharField(max_length=200)
    content = models.TextField(null=True)

    def __str__(self):
        return self.language


class ProjectPage(models.Model):
    pageTitle = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    language = models.ForeignKey(Language)
    content = models.TextField()
    images = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.pageTitle
