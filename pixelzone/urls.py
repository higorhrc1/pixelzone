from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('apps.Jogos.urls', namespace='jogos')),
    path('usuario/', include('apps.Usuario.urls', namespace='usuario')),
    path('genero/', include('apps.Genero.urls', namespace='genero')),
    path('reviews/', include('apps.Reviews.urls', namespace='reviews')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)