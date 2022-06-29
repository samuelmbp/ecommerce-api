from django.contrib import admin
from django.urls import path, include

# Change heading admin site
admin.site.site_header = 'Ecommerce Api'
admin.site.index_title = 'Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('store/', include('store.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('__debug__/', include('debug_toolbar.urls')),
]
