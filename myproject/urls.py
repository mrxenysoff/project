from accounts.views import AboutView
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('about/', AboutView.as_view(), name='about'),
    path('', include('blog.urls')),

]
