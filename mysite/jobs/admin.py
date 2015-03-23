__author__ = 'zobair'
from django.contrib import admin

from models import Jobs

class jobsAdmin(admin.ModelAdmin):
    class meta:
        model = Jobs


admin.site.register(Jobs, jobsAdmin)
