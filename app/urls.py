from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'
handler403 = 'core.views.permission_denied'

urlpatterns = [
    path('', include('students.urls', namespace='students')),
    path('admin/', admin.site.urls),
    path("select2/", include("django_select2.urls")),
]
