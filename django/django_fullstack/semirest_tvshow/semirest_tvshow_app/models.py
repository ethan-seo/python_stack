from django.db import models
from datetime import *

# Create your models here.
class ShowManager(models.Manager):
    def create_validator(self, reqPOST):
        errors = {}
        if len(reqPOST['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(reqPOST['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if len(reqPOST['description']) != 0 and len(reqPOST['description']) < 10:
            errors["description"] = "Description shoudl be at least 10 characters"
        if datetime.strptime(reqPOST['release_date'], '%Y-%m-%d') >= datetime.now():
            errors["date"] = "Release Date should be in the past"
        show_with_title = Show.objects.filter(title=reqPOST['title'])
        if len(show_with_title) > 0:
            errors["title_dup"] = "Show with the same Title already exists"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=30)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()