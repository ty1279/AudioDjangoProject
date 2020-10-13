from django.contrib import admin
from .models import Csv
from .models import Attribute

# Register your models here.
myModels = [Attribute, Csv]  # iterable list
admin.site.register(myModels)