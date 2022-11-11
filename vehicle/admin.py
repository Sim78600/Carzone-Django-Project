from django.contrib import admin
from vehicle.models import car
from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="50" style="border-radius:50px;"/>'.format(object.car_photo.url))

    list_display = ('id', 'thumbnail', 'car_title','state', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_title','state')
    search_fields = ('id','car_title', 'is_featured','description','doors')
    list_filter = ('state', 'price','condition','is_featured')
    list_editable = ['is_featured']

admin.site.register(car,CarAdmin)