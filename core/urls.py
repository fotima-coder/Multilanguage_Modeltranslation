from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.contrib import admin

# Tillarga ajralmaydigan umumiy havolalar
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')), # Tilni o'zgartirish uchun ichki API
]

# Tillarga qarab chiquvchi havolalar (/uz/, /en/, /ru/)
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
)

# Media va Statik fayllar uchun (Development rejimida)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)