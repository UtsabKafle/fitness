from django.contrib import admin

from home.views import dashboard, workout_view

# Register your models here.
from .models import *

admin.site.register(instruction)
admin.site.register(workout)
admin.site.register(images)
admin.site.register(transformation)
admin.site.register(set)
admin.site.register(rep)
admin.site.register(data)
admin.site.register(routine)
admin.site.register(date)