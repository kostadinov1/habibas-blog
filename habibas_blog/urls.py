
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('habibas_blog.accounts.urls')),
    path('', include('habibas_blog.core.urls')),
]
