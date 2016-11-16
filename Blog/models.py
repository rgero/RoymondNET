from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=100)
    content = models.TextField()
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Blog.Category')

    class Meta:
        ordering=['-created']

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('blog.views.post', args=[str(self.slug)])

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
