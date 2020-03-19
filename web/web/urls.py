"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from sucursales.urls import sucursal_patterns
from hook.urls import hook_patterns
from chat_app import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('chat/', views.chat, name='chat'),
    #Paths de Core
    path('', include('core.urls')),
    #Path de Sucursales
    path('sucursales/', include(sucursal_patterns)),
    #Paths de Admin
    path('admin/', admin.site.urls),
    #Paths de Authentication
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include(hook_patterns)),
   
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)