from django.db import models

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/%y/%m/%d")
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_link = models.URLField(max_length=100)
    joining_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    # def admin_photo(self):
    #     return mark_safe('<img src="{}"width="100"/>'.format(self.photo.url))
    # admin_photo.short_description = 'Image'
    # admin_photo.allow_tags = True

