from django.conf.urls import patterns, include, url

from profiles.views import ProfileView, EditProfileView

urlpatterns = patterns('',

    url(r'^(?P<slug>[-\w]+)/$', ProfileView.as_view(), name='profile'),
    url(r'^edit/(?P<slug>[-\w]+)/$', EditProfileView.as_view(), name='edit_profile'),

)