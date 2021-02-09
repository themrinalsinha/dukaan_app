from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from seller.api import product_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('seller/', include('seller.urls')),
    path('buyer/', include('buyer.urls')),

    # store access
    path("store/<str:store_slug>/", product_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
