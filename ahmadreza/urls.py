
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('rest.urls')),
    path('listings/', include('listings.urls')),
    path('account/', include('account.urls')),
    path('zarinpal/', include('zarinpal.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
