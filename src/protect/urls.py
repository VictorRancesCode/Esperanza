"""protect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from protect.core.views import landing, detail_slug, missing, found, ReportPerson

from django.conf import settings

app_name = "protect"
urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'api/', include('protect.core.api.urls')),
    path('admin/', admin.site.urls),
    url(r'^jet/', include('jet.urls', namespace='jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', namespace='jet-dashboard')),
    url(r'^$', landing, name='landing'),
    url(r'^missing/$', missing, name="missing_people"),
    url(r'found/$', found, name="found_people"),
    url(r'^detail/(?P<slug>.*)/$', detail_slug, name="detail"),
    url(r'^report/$', ReportPerson.as_view(), name="report"),
]
admin.site.site_header = "Personas Desaparecidas"

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.views import serve as static_serve

    staticpatterns = static(settings.STATIC_URL, view=static_serve)
    mediapatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = staticpatterns + mediapatterns + urlpatterns
