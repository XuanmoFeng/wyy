"""wyyWeb URL Configuration

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

from . import controler, test, co

urlpatterns = [
    url(r'spider/.*$', controler.spider, name='spider'),
    url(r'albumDetail/.*$', controler.album_detail, name='albumDetail'),
    url(r'album/.*$', controler.list_album, name='album'),
    url(r'^test/.*$', test.test, name='test'),
    url(r'^footer/', test.index),
    url(r'^search/.*$', test.search, name='search'),
    url(r'^song/.*$', controler.analysis, name='song'),
    url(r'^commentator/', test.commentator, name='commentator'),
    url(r'^comment/', test.comment, name='comment'),
    url(r'^level/.*$', co.level, name='level'),
    url(r'^sex/.*$', co.sex, name='sex'),
    url(r'wn/.*$',co.wn),
    url(r'^$', test.index)

]
