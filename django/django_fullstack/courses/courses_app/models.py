from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def create_validator(self, reqPOST):
        errors = {}
        if len(reqPOST['course_name']) < 5:
            errors["course_name"] = "Name must be more than 5 characters"
        if len(reqPOST['course_desc']) < 15:
            errors['course_desc'] = "Description must be more than 15 characters"
        return errors

class CourseDesc(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.OneToOneField(CourseDesc, related_name="course",on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()