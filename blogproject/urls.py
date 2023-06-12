
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from blogapp.views import manifest


urlpatterns = [
    path('manifest.json', manifest, name='manifest'),
    path('admin/', admin.site.urls),
    path('api/', include('blogapp.api_urls')),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve react pages for everything else
urlpatterns.append(re_path(r'^.*', TemplateView.as_view(template_name='index.html')),)