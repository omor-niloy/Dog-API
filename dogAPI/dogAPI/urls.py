from django.contrib import admin
from django.urls import path, include
from django.urls import path, re_path
from dogapp import views

urlpatterns = [
    path('', views.ApiRoot.as_view(), name='Home'),
    path('admin/', admin.site.urls, name='Admin-Panel'),
    path('api/', include('dogapp.urls'), name='Dog-API'),
    re_path(r'^.*$', views.ApiRoot.as_view(), name='catch-all'),
]