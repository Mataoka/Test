from django.conf.urls import include, url
from django.contrib import admin
from blogsitesi import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.gonderi_listesi, name='gonderi_listesi'),
]