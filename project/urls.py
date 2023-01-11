"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from matilde.views import (PostCrear, PostListar, PostDetalle, PostActualizar, index, UserSignUp, UserLogin, UserLogout, PostBorrar, AvatarActualizar, UserActualizar, MensajeCrear, MensajeDetalle, MensajeListar)


urlpatterns = [

   path('matilde/', index, name="matilde-index"),
   path('matilde/<int:pk>/detalle/', PostDetalle.as_view(), name="matilde-detalle"),
   path('matilde/listar/', PostListar.as_view(), name="matilde-listar"),
   path('matilde/crear/', staff_member_required(PostCrear.as_view()), name="matilde-crear"),
   path('matilde/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="matilde-borrar"),
   path('matilde/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="matilde-actualizar"),
   path('matilde/signup/', UserSignUp.as_view(), name ="matilde-signup"),
   path('matilde/login/', UserLogin.as_view(), name= "matilde-login"),
   path('matilde/logout/', UserLogout.as_view(), name="matilde-logout"),
   path('matilde/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="matilde-avatars-actualizar"),
   path('matilde/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="matilde-users-actualizar"),
   path('matilde/mensajes/crear/', MensajeCrear.as_view(), name="matilde-mensajes-crear"),
   path('matilde/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="matilde-mensajes-detalle"),
   path('matilde/mensajes/listar/', MensajeListar.as_view(), name="matilde-mensajes-listar"),
 ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
