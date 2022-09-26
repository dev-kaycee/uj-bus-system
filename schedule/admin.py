from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.Bus)
admin.site.register(models.Trip)