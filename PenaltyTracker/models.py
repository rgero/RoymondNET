from django.db import models

# Create your models here.
class SearchOptionGroup(models.Model):
  group_name = models.CharField(max_length=200)
  def __str__(self):
    return self.group_name
  
class Option(models.Model):
  option_name = models.CharField(max_length=200)
  parent_group = models.ForeignKey(SearchOptionGroup, on_delete=models.CASCADE)
  def __str__(self):
    return self.option_name