from django.contrib import admin
from .models import *

# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ["__str__", "email", "is_admin", "date_joined"]
    class Meta:
        model = UserInfo


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    class Meta:
        model = Category

class BlogAdmin(admin.ModelAdmin):
    list_display = ["__str__", "get_owner", "get_title", "get_is_publish", "get_content", "get_created", "get_last_modified"]
    class Meta:
        model = Blog



admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
