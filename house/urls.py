
# coding: utf-8

from django.conf.urls import url, include
from django.contrib import admin
from website.views import home
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    # 首页
    url(r'^', include('website.urls', namespace='website')),
    # 管理员后台
    url(r'^admin/', include('web.urls', namespace='web')),
    url(r'^h5$', TemplateView.as_view(template_name='longpage.html')),
    url(r'^wechatapi/', include('wechatapi.urls', namespace='wechatapi')),
    # 超级后台
    url(r'^superadmin/', admin.site.urls),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
