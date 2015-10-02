from django.conf.urls import include, url
from django.contrib import admin
from accounts import views
urlpatterns = [
    # Examples:
    url(r'^$', 'accounts.views.login', name='login'),
    url(r'^auth', 'accounts.views.auth_view', name='auth'),
    # url(r'^verification', views.VerificationToken.as_view(), name='VerificationToken'),
    url(r'^verify', 'accounts.views.verify_pass_token', name='verify_pass_token'),
    url(r'^invalid', 'accounts.views.invalid_login', name='invalid'),
    url(r'^loggedin', 'accounts.views.loggedin', name='loggedin'),
    url(r'^signup/$', views.SignUp.as_view(), name='signup'),
    url(r'^confirm/(?P<key>[\w]{32})/$', 'accounts.views.confirm_Registration', name='confirm_Registration'),
    url(r'^signup_success/$', 'accounts.views.signup_success', name='signup_success'),


    url(r'^admin/', include(admin.site.urls)),
]
