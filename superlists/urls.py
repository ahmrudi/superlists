from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'superlists.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'lists.views.home_page', name='home'),
    url(r'^lists/', include('lists.urls')),
    url(r'^notes/$', include('notes.urls')),
    url(r'^login/$', 'notes.views.login_user', name='login'),
    url(r'^logout/$', 'notes.views.logout_user', name='logout'),
    url(r'^sign-up/$', 'notes.views.sign_up', name='sign_up'),
    url(r'^error/$', 'notes.views.error', name='error'),
    url(r'^admin/', include(admin.site.urls)),
)
