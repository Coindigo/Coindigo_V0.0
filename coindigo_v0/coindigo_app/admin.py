from django.contrib import admin
from .models import *

# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ["__str__", "email", "is_admin", "date_joined"]
    class Meta:
        model = UserInfo




admin.site.register(UserInfo, UserInfoAdmin)
