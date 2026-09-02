from django.urls import path, include
from django.views.generic.base import RedirectView
from django.contrib import admin


urlpatterns = [
    path("admin/", admin.site.urls),
    path('hello/', include('hello.urls')),
    path('forum/', include('forum.urls')),
    path('', RedirectView.as_view(url='/forum/', permanent=False), name='home'),  # Redirect root URL to forum

]