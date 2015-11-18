"""chirper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from chirper import settings
from users.views import UserDonate

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^chirps/', include('chirp.urls')),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page':"/chirps/"}, name='logout'),
    url(r'^api/', include('api.urls')),
    url(r'^donate/$', UserDonate.as_view()),
    url('^', include('django.contrib.auth.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
