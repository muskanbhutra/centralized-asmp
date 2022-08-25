from django.contrib import admin
from .models import Speaker, Student


admin.site.register(Student)
admin.site.register(Speaker)