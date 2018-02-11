"""test_gps URL Configuration

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
from recuperer.views import affiche_data

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<id1>\d{1,6})\.(?P<id2>\d{1,6})/(?P<id3>\d{1,6})\.(?P<id4>\d{1,6})/(?P<id5>\d{1,6})\.(?P<id6>\d{1,6})/(?P<year>\d{4})/(?P<month>\d{2,4})/(?P<day>\d{2,4})/(?P<hours>\d{2,4})/(?P<m>\d{2,4})/(?P<sec>\d{2,4})/$', affiche_data),
]