"""SeatManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from stores import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^search/$', views.search, name='search'),
    url(r'^autocomplete/$', views.autocomplete, name='autocomplete'),
    url(r'^update_db/', views.update_db, name='update_db'),
    url(r'^store_status/manager/(?P<store_name>[\w-]+)/$', views.store_status, name='store_status'),
    url(r'^store_status/(?P<store_name>[\w-]+)/$', views.customer, name='customer'),

]
