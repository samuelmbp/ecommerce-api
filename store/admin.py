from django.contrib import admin
from . import models

# Register store models
admin.site.register(models.Collection)

admin.site.register(models.Product)