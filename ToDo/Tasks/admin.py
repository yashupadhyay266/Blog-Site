from django.contrib import admin

# Register your models here.
from Tasks.models import Task,ImageFromUser

admin.site.register(Task)
admin.site.register(ImageFromUser)