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
from ejemplo.views import ( FamiliarBorrar, index, mostrar_familiares, BuscarFamiliar, AltaFamiliar, FamiliarActualizar, FamiliarDetalle, FamiliarList, FamiliarCrear, )
from matilde.views import (PostCrear, PostListar, PostDetalle, PostActualizar, index, UserSignUp, UserLogin, UserLogout, PostBorrar, AvatarActualizar, UserActualizar, MensajeCrear, MensajeDetalle, MensajeListar)
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
      path('admin/', admin.site.urls),
      path('saludar/', index),
      path('mi-familia/', mostrar_familiares),
      path('mi-familia/buscar', BuscarFamiliar.as_view()), 
      path('mi-familia/alta', AltaFamiliar.as_view()),
      path('mi-familia/actualizar/<int:pk>', FamiliarActualizar.as_view()),
      path('panel-familia/<int:pk>/detalle', FamiliarDetalle.as_view()),
      path('panel-familia/', FamiliarList.as_view()), 
      path('panel-familia/crear', FamiliarCrear.as_view()),
      path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()), 
      path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()), # NUEVA RUTA PARA LISTAR FAMILIAR
      path('ejemplo-dos/', index, name="ejemplo-dos-index"),
      path('ejemplo-dos/listar/posts', PostListar.as_view(), name="ejemplo-dos-listar"),
      path('ejemplo-dos/crear/', PostCrear.as_view(), name="ejemplo-dos-crear"),
       path('success_updated_message/',TemplateView.as_view(template_name="ejemplo/success_updated_message.html")),
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
