from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'bospas.views.home', name='home'),
    url(r'^', include('inicio.urls', namespace="inicio")),
    url(r'^admin/', include(admin.site.urls)),
]
