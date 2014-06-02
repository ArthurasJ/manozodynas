from django.conf.urls import patterns, url
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import index_view, login_view, words_view, words_del_view, translations_view, translation_add_view

urlpatterns = patterns('',
    url(r'^$', index_view, name='index'),
    url(r'^login$', login_view, name='login'),
    url(r'^words$', words_view, name='words'),
    url(r'^worddel/(?P<key>\d)$', words_del_view, name='word_del'),
    url(r'^translations/(?P<key>\d)$', translations_view, name='translations'),
    url(r'^translationadd/', translation_add_view, name='translations'),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
)
