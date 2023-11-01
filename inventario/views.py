from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


from inventario.forms  import EmpresaForm, PersonalForm, SucursalForm,GruposProveedorForm, InventarioForm, ItemsInventarioForm,UnidadForm,ArticulosForm,LineasArticulosForm, MarcasForm,SublineasArticulosForm, UsuarioProfileForm
from django.urls import reverse_lazy

from inventario.models import Empresa, Personal,Sucursal,GruposProveedor,Inventarios, ItemsInventario,UnidadesMedida,Usuario,Articulos,LineasArticulos, Marcas, SublineasArticulos




# Create your views here.

def index(request):
    num_articulos= Articulos.objects.all().count
    num_usuarios =Usuario.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session ['num_visits'] = num_visits +1
    context={
        'num_articulos': num_articulos,
        'num_usuarios': num_usuarios,
        'num_visits': num_visits,
    }
    return render(request, 'index/index.html', context=context)


class EmpresaRegistro(CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa/nuevo_empresa.html'  
    success_url = reverse_lazy('empresa_lista') 

class EmpresaLista(ListView):
    model = Empresa
    template_name = 'empresa/empresa_lista.html' 
    ontext_object_name = 'empresas'

class EmpresaActualizar(UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa/nuevo_empresa.html'  
    success_url = reverse_lazy('empresa_lista')  

class EmpresaEliminar(DeleteView):
    model = Empresa
    template_name = 'empresa/empresa_eliminar.html'
    success_url = reverse_lazy('empresa_lista')  

class SucursalRegistro(CreateView):
    model = Sucursal
    form_class = SucursalForm
    template_name = 'sucursal/nuevo_sucursal.html'  
    success_url = reverse_lazy('sucursal_lista')  

class SucursalLista(ListView):
    model = Sucursal
    template_name = 'sucursal/sucursal_lista.html'  
    ontext_object_name = 'sucursal'

class SucursalActualizar(UpdateView):
    model = Sucursal
    form_class = SucursalForm
    template_name = 'sucursal/nuevo_sucursal.html'  
    success_url = reverse_lazy('sucursal_lista')  

class SucursalEliminar(DeleteView):
    model = Sucursal
    template_name = 'sucursal/sucursal_eliminar.html'  
    success_url = reverse_lazy('sucursal_lista')  
    
class PersonalRegistro(CreateView):
    model = Personal
    form_class = PersonalForm
    template_name = 'personal/nuevo_personal.html'  
    success_url = reverse_lazy('personal_lista') 
 
class PersonalLista(ListView):
    model = Personal
    template_name = 'personal/personal_lista.html' 
    ontext_object_name = 'personal'

class PersonalActualizar(UpdateView):
    model = Personal
    form_class = PersonalForm
    template_name = 'personal/nuevo_personal.html'  
    success_url = reverse_lazy('personal_lista')  

class PersonalEliminar(DeleteView):
    model = Personal
    template_name = 'personal/personal_eliminar.html'
    success_url = reverse_lazy('personal_lista')  
    
       
class GruposProveedorRegistro(CreateView):
    model = GruposProveedor 
    form_class = GruposProveedorForm  
    template_name = 'gruposproveedor/nuevo_grupos_proveedor.html'  
    success_url = reverse_lazy('grupos_proveedor_lista') 

class GruposProveedorLista(ListView):
    model = GruposProveedor  
    template_name = 'gruposproveedor/grupos_proveedor_lista.html'  
    context_object_name = 'grupos_proveedor'  

class GruposProveedorActualizar(UpdateView):
    model = GruposProveedor  
    form_class = GruposProveedorForm  
    template_name = 'gruposproveedor/nuevo_grupos_proveedor.html' 
    success_url = reverse_lazy('grupos_proveedor_lista')  

class GruposProveedorEliminar(DeleteView):
    model = GruposProveedor  
    template_name = 'gruposproveedor/grupos_proveedor_eliminar.html'  
    success_url = reverse_lazy('grupos_proveedor_lista')  

class UnidadRegistro(CreateView):
    model = UnidadesMedida
    form_class = UnidadForm
    template_name = 'unidadesmedida/nuevo_unidades_medida.html'
    success_url = reverse_lazy('unidades_medida_lista')

class UnidadLista(ListView):
    model = UnidadesMedida
    template_name = 'unidadesmedida/unidades_medida_lista.html'
    ontext_object_name = "unidades"

class UnidadActualizar(UpdateView):
    model = UnidadesMedida
    form_class = UnidadForm
    template_name = 'unidadesmedida/nuevo_unidades_medida.html'
    succes_url = reverse_lazy ('unidades_medida_lista')

class UnidadEliminar(DeleteView):
    model = UnidadesMedida
    template_name = 'unidadesmedida/unidades_medida_eliminar.html'
    succes_url = reverse_lazy('unidades_medida_lista')


#LINEASARTICULOS

class LineasArticulosRegistro(CreateView):
    model = LineasArticulos
    form_class = LineasArticulosForm
    template_name = 'lineasArticulos/nuevo_lineasArticulos.html'  
    success_url = reverse_lazy('lineasArticulos_lista') 

class LineasArticulosLista(ListView):
    model = LineasArticulos
    template_name = 'lineasArticulos/lineasArticulos_lista.html' 
    ontext_object_name = 'lineasArticulos'

class LineasArticulosActualizar(UpdateView):
    model = LineasArticulos
    form_class = LineasArticulosForm
    template_name = 'lineasArticulos/nuevo_lineasArticulos.html'  
    success_url = reverse_lazy('lineasArticulos_lista')  

class LineasArticulosEliminar(DeleteView):
    model = LineasArticulos
    template_name = 'lineasArticulos/lineasArticulos_eliminar.html'
    success_url = reverse_lazy('lineasArticulos_lista')  


#SUBLINEASARTICULOS

class SublineasArticulosRegistro(CreateView):
    model = SublineasArticulos
    form_class = SublineasArticulosForm
    template_name = 'sublineasArticulos/nuevo_sublineasArticulos.html'  
    success_url = reverse_lazy('sublineasArticulos_lista') 

class SublineasArticulosLista(ListView):
    model = SublineasArticulos
    template_name = 'sublineasArticulos/sublineasArticulos_lista.html' 
    ontext_object_name = 'sublineasArticulos'

class SublineasArticulosActualizar(UpdateView):
    model = SublineasArticulos
    form_class = SublineasArticulosForm
    template_name = 'sublineasArticulos/nuevo_sublineasArticulos.html'  
    success_url = reverse_lazy('sublineasArticulos_lista')  

class SublineasArticulosEliminar(DeleteView):
    model = SublineasArticulos
    template_name = 'sublineasArticulos/sublineasArticulos_eliminar.html'
    success_url = reverse_lazy('sublineasArticulos_lista') 

#MARCAS

class MarcasRegistro(CreateView):
    model = Marcas
    form_class = MarcasForm
    template_name = 'marcas/nuevo_marcas.html'  
    success_url = reverse_lazy('marcas_lista') 

class MarcasLista(ListView):
    model = Marcas
    template_name = 'marcas/marcas_lista.html' 
    ontext_object_name = 'marcas'

class MarcasActualizar(UpdateView):
    model = Marcas
    form_class = MarcasForm
    template_name = 'marcas/nuevo_marcas.html'  
    success_url = reverse_lazy('marcas_lista')  

class MarcasEliminar(DeleteView):
    model = Marcas
    template_name = 'marcas/marcas_eliminar.html'
    success_url = reverse_lazy('marcas_lista') 


#ARTICULOS

class ArticulosRegistro(CreateView):
    model = Articulos
    form_class = ArticulosForm
    template_name = 'articulos/nuevo_articulos.html'  
    success_url = reverse_lazy('articulos_lista') 

class ArticulosLista(ListView):
    model = Articulos
    template_name = 'articulos/articulos_lista.html' 
    ontext_object_name = 'articulos'

class ArticulosActualizar(UpdateView):
    model = Articulos
    form_class = ArticulosForm
    template_name = 'articulos/nuevo_articulos.html'  
    success_url = reverse_lazy('articulos_lista')  

class ArticulosEliminar(DeleteView):
    model = Articulos
    template_name = 'articulos/articulos_eliminar.html'
    success_url = reverse_lazy('articulos_lista') 


class UsuarioRegistro(CreateView):
    model = Usuario
    form_class = UsuarioProfileForm
    template_name = 'usuario/nuevo_usuario.html'  
    success_url = reverse_lazy('usuario_lista')  


class UsuarioLista(ListView):
    model = Usuario
    template_name = 'usuario/usuario_lista.html'
    ontext_object_name = 'usuario'

class UsuarioActualizar(UpdateView):
    model = Usuario
    form_class = UsuarioProfileForm
    template_name ='usuario/nuevo_usuario.html'
    success_url = reverse_lazy('usuario_lista')

class UsuarioEliminar(DeleteView):
    model = Usuario
    template_name = 'usuario/usuario_eliminar.html'  
    success_url = reverse_lazy('usuario_lista')  
    
    


class InventarioRegistro(CreateView):
    model = Inventarios
    form_class=InventarioForm
    template_name='inventarios/nuevo_inventario.html'
    success_url=reverse_lazy('inventario_lista')

class InventarioLista(ListView):
    model = Inventarios
    template_name='inventarios/inventario_lista.html'
    ontext_object_name='inventarios'

class InventarioActualizar(UpdateView):
    model= Inventarios
    form_class=InventarioForm
    template_name='inventarios/nuevo_inventario.html'
    success_url=reverse_lazy('inventario_lista')

class InventarioEliminar(DeleteView):
    model= Inventarios
    template_name='inventarios/inventario_eliminar.html'
    success_url=reverse_lazy('inventario_lista')

class ItemsInventarioRegistro(CreateView):
    model=ItemsInventario
    form_class=ItemsInventarioForm
    template_name='itemsinventario/nuevo_itemsinventario.html'
    success_url=reverse_lazy('nuevo_itemsinventario')

class ItemsInventarioLista(ListView):
    model=ItemsInventario
    template_name='itemsinventario/itemsinventario_lista.html'
    ontext_object_name='itemsinventario'

class ItemsInventarioActualizar(UpdateView):
    model=ItemsInventario
    form_class=ItemsInventarioForm
    template_name='itemsinventario/nuevo_itemsinventario.html'
    success_url=reverse_lazy('itemsinventario_lista')

class ItemsInventarioEliminar(DeleteView):
    model=ItemsInventario
    template_name='itemsinventario/itemsinventario_eliminar.html'
    success_url=reverse_lazy('itemsinventario_lista')
