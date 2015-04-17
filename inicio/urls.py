from django.conf.urls import url

from inicio import views

urlpatterns = [
    url(r'^$', views.ViewHome.as_view(), name='home'),
    url(r'^about/$', views.ViewAbout.as_view(), name='about'),
    url(r'^galery/$', views.ViewGalery.as_view(), name='gallery'),
    url(r'^info/$', views.ViewInfo.as_view(), name='info')
    # url(r'^contact/$', views.ViewDeportes.as_view(), name='contact'),
]
