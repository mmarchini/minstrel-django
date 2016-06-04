"""minstrel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^music/(?P<session_id>\d{1,50})/(?P<composition_id>\d{1,50})/$', views.music, name='music'),  # NOQA
    url(r'^detailed_composer/$', views.index, name='detailed_composer'),  # NOQA
    url(r'^set_csrf/$', views.set_csrf, name='set_csrf'),  # NOQA
    url(r'^compose/$', views.new_compose, name='compose'),  # NOQA
    url(r'^$', views.new_screen, name='index'),
]
