from __future__ import unicode_literals
from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def create_validator(self, reqPOST):
        errors = {}
        NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(reqPOST['first_name']) < 2 or not NAME_REGEX.match(reqPOST["first_name"]):
            errors["first_name"] = "First name should be at least 2 charaters and letters only"
        if len(reqPOST['last_name']) < 2 or not NAME_REGEX.match(reqPOST["last_name"]):
            errors["last_name"] = "Last name should be at least 2 charaters and letters only"
        if len(reqPOST['email']) < 8:
            errors["email"] = "Email needs to be longer."
        if len(reqPOST['password']) < 8:
            errors['password'] = "Passwords must be at least 8 charaters"
        if reqPOST['password'] != reqPOST['password_conf']:
            errors['password_conf'] = "Passwords need to match"
        if not EMAIL_REGEX.match(reqPOST["email"]):
            errors['regex'] = "Email is not in correct format"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()