from __future__ import unicode_literals
from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def create_validator(self, reqPOST):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(reqPOST['user_name']) < 5:
            errors["name"] = "User name should be at least 5 charaters"
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
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class KoalaManager(models.Manager):
    def create_validator(self, reqPOST):
        errors = {}
        if len(reqPOST['koala_name']) < 3:
            errors["koala_name"] = "Koala name is too short."
        if len(reqPOST['talent']) < 6:
            errors['talent'] = "Talent is too short."
        koalas_with_same_name = Koala.objects.filter(name=reqPOST['koala_name'])
        if len(koalas_with_same_name) > 0:
            errors['duplicate'] = "Name already taken, pick another one."
        return errors

class Koala(models.Model):
    name = models.CharField(max_length=40)
    talent = models.TextField()
    user = models.ForeignKey(User, related_name="koalas_owned", on_delete=models.CASCADE)
    users_votes = models.ManyToManyField(User, related_name="voted_koalas")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = KoalaManager()

#Self-join
# class User(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     friendships = models.ManyToManyField("self")