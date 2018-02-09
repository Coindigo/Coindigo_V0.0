from django.db import models
from django.contrib.auth.models import User

import datetime
# Create your models here.


class UserInfo(models.Model):
    user = models.OneToOneField(User, related_name='userinfo', on_delete = models.CASCADE)
    user_image = models.ImageField(blank = True, null = True, upload_to = "static/media")
    about = models.TextField(blank = True, null = True)
    contact_info = models.TextField(blank = True, null = True)
    def __str__(self):
        return str(self.user)
    def email(self):
        return self.user.email
    def is_admin(self):
        return self.user.is_staff
    def date_joined(self):
        return self.user.date_joined


class Category(models.Model):
    """Scam of the Week, ..."""
    name = models.TextField()
    def __str__(self):
        return str(self.name)


class Blog(models.Model):
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=True)
    title = models.TextField(default = "Untitled",blank = False, null = False)
    content = models.TextField(blank = True, null = True)
    category = models.ForeignKey(Category, blank = True, null = True, on_delete=False)
    blog_image = models.ImageField(blank = True, null = True, upload_to = "static/media")
    created = models.DateTimeField(default= datetime.datetime.now())
    is_publish = models.BooleanField(default= False, blank = False, null = False)
    last_modified = models.DateTimeField(default= datetime.datetime.now())

    def __str__(self):
        return str(self.category)
    def get_title(self):
        return str(self.title)
    def get_is_publish(self):
        return str(self.is_publish)
    def get_content(self):
        return self.content
    def get_owner(self):
        return self.owner
    def get_created(self):
        return str(self.created)
    def get_last_modified(self):
        return str(self.last_modified)
