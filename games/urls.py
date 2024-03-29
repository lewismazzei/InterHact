"""games URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from sudoku import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^new/(?P<token>[A-Za-z0-9]+)/(?P<email>[A-Za-z0-9.@-]+)/$', views.new),
    url(r'^play/(?P<game_id>[0-9]+)/$', views.play),
    url(r'^join/(?P<game_id>[0-9]+)/(?P<email>[A-Za-z0-9.@-]+)/(?P<token>[A-Za-z0-9]+)/(?P<room>[A-Za-z0-9]+)/$', views.join),
    url(r'^save/(?P<game_id>[0-9]+)/(?P<token>[A-Za-z0-9]+)/(?P<score>[0-9]+)/$', views.save),
    url(r'^results/$', views.results),
    url(r'^patients/$', views.patients),
]
