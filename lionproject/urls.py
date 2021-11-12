"""lionproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from blog.views import home, loading
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name="home"),
    path('', loading, name="loading"),
    path('blog/', include('blog.urls')),
    path('drinking/', include('drinking.urls')),
    path('user/', include('user.urls')),
<<<<<<< HEAD
=======
    path('community/', include('community.urls')),
    path('commentcrud/', include('commentcrud.urls')),

>>>>>>> fab298292d5b5df592b7c57cf6c1976e00171f3b
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

