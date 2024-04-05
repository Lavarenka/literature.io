"""
URL configuration for literature project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from blog.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('add_book/', include('add_books.urls')), # добавить книгу
    path('users/', include('users.urls', namespace="users")), # добавить книгу/ namespace="users" пространство имен
    path("__debug__/", include("debug_toolbar.urls")), # дебагер
]

if settings.DEBUG:
    # для отображения файлов в режиме отдладки

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# обработчик 404
handler404 = page_not_found
