# coding: utf-8

from django.conf.urls import url

from website.views import (
    home,
)

# 管理后台
urlpatterns = [
    # 首页
    url(r'^$', home.index, name='home_index'),
]
