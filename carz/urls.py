from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('wheel.urls')),
    path('cars/',include('vehicle.urls')),
    path('accounts/',include('accounts.urls')),
    path('socialaccounts/',include('allauth.urls')),
    path('contacts/',include('contact.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)