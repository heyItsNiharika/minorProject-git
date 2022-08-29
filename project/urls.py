from django.contrib import admin
from django.urls import path,  include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),   #'' means home page. when a user will open the home page it will be redirected to urls in pages
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

