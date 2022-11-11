from msilib.schema import Class
from django.contrib import admin
from wheel.models import Team
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def Photo(self,object):
        return format_html('<img src="{}" width="50" style="border-radius:50px" />'.format(object.photo.url))
    
    list_display= ('id','Photo','first_name','last_name','designation','joining_date')
    list_display_links = ('id','first_name','designation','joining_date','Photo')
    search_fields = ('id','first_name','last_name','designation','joining_date')
    list_filter = ('designation','joining_date')

admin.site.register(Team,TeamAdmin)
