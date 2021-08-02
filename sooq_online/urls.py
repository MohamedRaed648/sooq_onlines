
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("sooq.urls")),
    path('',include("auth_sooq.urls")),

    #REST FRAMWORK URLS
    path('api/',include('sooq.api_sooq.urls')),
    path('api_register/',include('auth_sooq.api_auth.urls'))
]
