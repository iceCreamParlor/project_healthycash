"""healthycash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, PasswordResetView, LogoutView

from .views import home
from profiles.views import RegisterViewNormal, RegisterViewMaster

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^aboutus/', TemplateView.as_view(template_name = 'aboutus.html'), name='aboutus'),

    url(r'^password_reset/', PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),    
    url(r'^healthclub/', include('healthclub.urls', namespace='healthclub')),
    url(r'^profiles/', include('profiles.urls', namespace='profiles')),
    url(r'^register/', TemplateView.as_view(template_name='registration/register.html'), name='register'),
    url(r'^register_normal/', RegisterViewNormal.as_view(), name='register_normal'),
    url(r'^register_master/', RegisterViewMaster.as_view(), name='register_master'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)