from django.contrib import admin
from django.urls import path
from base.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('view', view_item)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
