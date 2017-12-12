from django.contrib import admin

from .models import Profile, School, Degree

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'program', 'grad_year',
                    'resume', 'viewable')

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('abbrev', 'name')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Degree)
