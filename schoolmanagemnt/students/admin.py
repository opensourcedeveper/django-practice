from django.contrib import admin
from .models import Student,Car  # Import your models here

# Register your models here
admin.site.register(Student)
admin.site.register(Car)
# admin.site.register(YourModel2)