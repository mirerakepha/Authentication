from django.contrib import admin
from django.urls import path, include  # include is key to link to your app
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authenticationapp.urls')),  # connects to your app's URLs
]

# Serve media files like profile pictures during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
