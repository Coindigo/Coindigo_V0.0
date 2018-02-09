from django.db import models
from django.contrib.auth.models import User
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
