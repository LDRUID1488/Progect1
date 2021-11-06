from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Users)
admin.site.register(Project)
admin.site.register(Exercise)

