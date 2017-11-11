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
    url(r'^create_game/(?P<token>[A-Za-z0-9]+)/(?P<email>[A-Za-z0.9@.]+)/$', views.create_game),
    url(r'^add_user/$', views.add_user),
    url(r'^save_game/$', views.save_game),
    url(r'^show_board/(?P<game_id>[0-9]+)/(?P<token>[A-Za-z0-9]+)/$', views.show_board),
]
