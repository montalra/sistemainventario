from django.urls import path
from .views import EmpresaRegistro,EmpresaLista, EmpresaActualizar, EmpresaEliminar
from .views import SucursalRegistro, SucursalLista, SucursalActualizar, SucursalEliminar
from .views import PersonalRegistro, PersonalLista, PersonalActualizar, PersonalEliminar
from .views import GruposProveedorRegistro, GruposProveedorLista, GruposProveedorActualizar, GruposProveedorEliminar
from .views import InventarioRegistro,InventarioLista, InventarioActualizar, InventarioEliminar
from .views import ItemsInventarioRegistro,ItemsInventarioLista,ItemsInventarioActualizar,ItemsInventarioEliminar
from .views import UnidadRegistro, UnidadLista, UnidadActualizar, UnidadEliminar
from .views import UsuarioRegistro,  UsuarioLista,  UsuarioActualizar,  UsuarioEliminar
from .views import LineasArticulosLista, LineasArticulosRegistro, LineasArticulosActualizar, LineasArticulosEliminar
from .views import SublineasArticulosLista, SublineasArticulosRegistro, SublineasArticulosActualizar, SublineasArticulosEliminar
from .views import MarcasLista, MarcasRegistro, MarcasActualizar, MarcasEliminar
from .views import ArticulosActualizar, ArticulosEliminar, ArticulosLista, ArticulosRegistro
from .import views
urlpatterns = [

    path ('', views.index, name='index'),

    path('empresa/nueva/', EmpresaRegistro.as_view(), name='nuevo_empresa'),
    path('empresa/listar/', EmpresaLista.as_view(), name='empresa_lista'),
    path('empresa/editar/<uuid:pk>/', EmpresaActualizar.as_view(), name='empresa_actualizar'),
    path('empresa/eliminar/<uuid:pk>', EmpresaEliminar.as_view(), name='empresa_eliminar'),

    path('sucursal/nueva/', SucursalRegistro.as_view(), name='nuevo_sucursal'),
    path('sucursal/listar/', SucursalLista.as_view(), name='sucursal_lista'),
    path('sucursal/editar/<uuid:pk>', SucursalActualizar.as_view(), name='sucursal_actualizar'),
    path('sucursal/eliminar/<uuid:pk>/', SucursalEliminar.as_view(), name='sucursal_eliminar'),
  
    path('personal/nueva/', PersonalRegistro.as_view(), name='nuevo_personal'),
    path('personal/listar/', PersonalLista.as_view(), name='personal_lista'),
    path('personal/editar/<uuid:pk>/', PersonalActualizar.as_view(), name='personal_actualizar'),
    path('personal/eliminar/<uuid:pk>/', PersonalEliminar.as_view(), name='personal_eliminar'),

    path('grupos_proveedor/nueva/', GruposProveedorRegistro.as_view(), name='nuevo_grupos_proveedor'),
    path('grupos_proveedor/listar/', GruposProveedorLista.as_view(), name='grupos_proveedor_lista'),
    path('grupos_proveedor/editar/<uuid:pk>/', GruposProveedorActualizar.as_view(), name='grupos_proveedor_actualizar'),
    path('grupos_proveedor/eliminar/<uuid:pk>/', GruposProveedorEliminar.as_view(), name='grupos_proveedor_eliminar'),

    path('unidad/nueva/', UnidadRegistro.as_view(), name='nuevo_unidades_medida'),
    path('unidad/listar/', UnidadLista.as_view(), name='unidades_medida_lista'),
    path('unidad/editar/<uuid:pk>/', UnidadActualizar.as_view(), name='unidades_medida_actualizar'),
    path('unidad/eliminar/<uuid:pk>', UnidadEliminar.as_view(), name= 'unidades_medida_eliminar'),

     path('lineasArticulos/nueva/', LineasArticulosRegistro.as_view(), name='nuevo_lineasArticulos'),
    path('lineasArticulos/listar/', LineasArticulosLista.as_view(), name='lineasArticulos_lista'),
    path('lineasArticulos/editar/<uuid:pk>/', LineasArticulosActualizar.as_view(), name='lineasArticulos_actualizar'),
    path('lineasArticulos/eliminar/<uuid:pk>/', LineasArticulosEliminar.as_view(), name='lineasArticulos_eliminar'), 


    path('sublineasArticulos/nueva/', SublineasArticulosRegistro.as_view(), name='nuevo_sublineasArticulos'),
    path('sublineasArticulos/listar/', SublineasArticulosLista.as_view(), name='sublineasArticulos_lista'),
    path('sublineasArticulos/actualizar/<uuid:pk>/', SublineasArticulosActualizar.as_view(), name='sublineasArticulos_actualizar'),
    path('sublineasArticulos/eliminar/<uuid:pk>/', SublineasArticulosEliminar.as_view(), name='sublineasArticulos_eliminar'),


    path('marcas/nueva/', MarcasRegistro.as_view(), name='nuevo_marcas'),
    path('marcas/listar/', MarcasLista.as_view(), name='marcas_lista'),
    path('marcas/actualizar/<uuid:pk>/', MarcasActualizar.as_view(), name='marcas_actualizar'),
    path('marcas/eliminar/<uuid:pk>/', MarcasEliminar.as_view(), name='marcas_eliminar'),  


    path('articulos/nueva/', ArticulosRegistro.as_view(), name='nuevo_articulos'),
    path('articulos/listar/', ArticulosLista.as_view(), name='articulos_lista'),
    path('articulos/actualizar/<uuid:pk>/', ArticulosActualizar.as_view(), name='articulos_actualizar'),
    path('articulos/eliminar/<uuid:pk>/', ArticulosEliminar.as_view(), name='articulos_eliminar'),


    path('inventarios/nueva/',InventarioRegistro.as_view(),name='nuevo_inventario'),
    path('inventarios/listar/',InventarioLista.as_view(),name='inventario_lista'),
    path('inventarios/editar/<uuid:pk>',InventarioActualizar.as_view(),name='inventario_actualizar'),
    path('inventarios/eliminar/<uuid:pk>',InventarioEliminar.as_view(),name='inventario_eliminar'),

    path('itemsinventario/nueva/',ItemsInventarioRegistro.as_view(), name='nuevo_itemsinventario'),
    path('itemsinventario/listar/',ItemsInventarioLista.as_view(),name='itemsinventario_lista'),
    path('itemsinventario/editar/<uuid:pk>',ItemsInventarioActualizar.as_view(),name='itemsinventario_actualizar'),
    path('itemsinventario/eliminar/<uuid:pk>',ItemsInventarioEliminar.as_view(),name='itemsinventario_eliminar'),

    path('usuario/nueva/', UsuarioRegistro.as_view(), name='nuevo_usuario'),
    path('usuario/listar/', UsuarioLista.as_view(), name='usuario_lista'),
    path('usuario/editar/<int:pk>/', UsuarioActualizar.as_view(), name='usuario_actualizar'),
    path('eliminar/<int:pk>/', UsuarioEliminar.as_view(), name='usuario_eliminar'),


]

