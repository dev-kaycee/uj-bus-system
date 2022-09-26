from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'UJ Bus Service'                    # default: "Django Administration"
admin.site.index_title = 'Adminsitration'                 # default: "Site administration"````
admin.site.site_title = 'UJ BUS SERVICE'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('user_auth.urls')),
]
