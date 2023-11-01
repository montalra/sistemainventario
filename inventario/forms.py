from django import forms
from .models import Empresa,Sucursal,Personal, GruposProveedor,ItemsInventario,Inventarios,Articulos,UnidadesMedida,LineasArticulos, Marcas,SublineasArticulos,Articulos, Usuario


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nro_documento', 'razon_social', 'direccion']
        widgets = {
            'nro_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'razon_social': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PersonalForm(forms.ModelForm):
    empresa = forms.ModelChoiceField(
        queryset=Empresa.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def _init_(self, *args, **kwargs):
        super(PersonalForm, self)._init_(*args, **kwargs)

        self.fields['empresa_Id'].label_from_instance = lambda obj: f"{obj.razon_social}"

    class Meta:
        model = Personal
        fields = ['nombre_personal', 'direccion_personal' ,'tipo_documento', 'nro_documento']
        widgets = {
            'nombre_personal': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_personal': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'nro_documento': forms.TextInput(attrs={'class': 'form-control'}),
}
        
 
class SucursalForm(forms.ModelForm):
    empresa = forms.ModelChoiceField(
        queryset=Empresa.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super(SucursalForm, self).__init__(*args, **kwargs)

        self.fields['empresa'].label_from_instance = lambda obj: f"{obj.razon_social}"

    class Meta:
        model = Sucursal
        fields = ['empresa', 'nombre_comercial', 'direccion']
        widgets = {
            'nombre_comercial': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }


class GruposProveedorForm(forms.ModelForm):
    empresa = forms.ModelChoiceField(
        queryset=Empresa.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    personal = forms.ModelChoiceField(
        queryset=Personal.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    def _init_(self, *args, **kwargs):
        super(GruposProveedorForm, self)._init_(*args, **kwargs)

        self.fields['empresa_Id'].label_from_instance = lambda obj: f"{obj.razon_social}"
        self.fields['personal_id'].label_from_instance = lambda obj: f"{obj.nombre_personal}"

    class Meta:
        model = GruposProveedor
        fields = [ 'codigo_grupo', 'grupo_descripcion','activo']
        widgets = {
            'codigo_grupo': forms.TextInput(attrs={'class': 'form-control'}),
            'grupo_descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UnidadForm(forms.ModelForm):
    class Meta:
        model = UnidadesMedida
        fields = ['unidad_nombre']
        widgets = {
            'unidad_nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class LineasArticulosForm(forms.ModelForm):
    personal = forms.ModelChoiceField(
        queryset=Personal.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    gruposproveedor = forms.ModelChoiceField(
        queryset=GruposProveedor.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def _init_(self, *args, **kwargs):
        super(LineasArticulosForm, self)._init_(*args, **kwargs)

        self.fields['personal_id'].label_from_instance = lambda obj: f"{obj.nombre_personal}"
        self.fields['grupo_id'].label_from_instance = lambda obj: f"{obj.codigo_grupo}"

    class Meta:
        model = LineasArticulos
        fields = [ 'codigo_linea', 'linea_descripcion','activo']
        widgets = {
            'codigo_linea': forms.TextInput(attrs={'class': 'form-control'}),
            'linea_descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'activo': forms.TextInput(attrs={'class': 'form-control'}),
}
        

class SublineasArticulosForm(forms.ModelForm):
    lineas_articulos = forms.ModelChoiceField(
        queryset=LineasArticulos.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def _init_(self, *args, **kwargs):
        super(SublineasArticulosForm, self)._init_(*args, **kwargs)

        self.fields['linea_id'].label_from_instance = lambda obj: f"{obj.codigo_linea}"

    class Meta:
        model = SublineasArticulos
        fields = [ 'codigo_sublinea', 'sublinea_descripcion', 'estado']
        widgets = {
            'codigo_sublinea': forms.TextInput(attrs={'class': 'form-control'}),
            'sublinea_descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
}
        

class MarcasForm(forms.ModelForm):
    class Meta:
        model = Marcas
        fields = [ 'codigo_marca', 'marca_nombre']
        widgets = {
            'codigo_marca': forms.TextInput(attrs={'class': 'form-control'}),
            'marca_nombre': forms.TextInput(attrs={'class': 'form-control'}),
}
   
class ArticulosForm(forms.ModelForm):
    unidadesmedida = forms.ModelChoiceField(
        queryset=UnidadesMedida.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    gruposproveedor = forms.ModelChoiceField(
        queryset=GruposProveedor.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    lineasarticulos = forms.ModelChoiceField(
        queryset=LineasArticulos.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    sublineasarticulos = forms.ModelChoiceField(
        queryset=SublineasArticulos.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    empresa = forms.ModelChoiceField(
        queryset=Empresa .objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    marcas = forms.ModelChoiceField(
        queryset=Marcas.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )


    def _init_(self, *args, **kwargs):
        super(ArticulosForm, self)._init_(*args, **kwargs)

        self.fields['unidad_medida_id'].label_from_instance = lambda obj: f"{obj.unidad_nombre}"
        self.fields['grupo_id'].label_from_instance = lambda obj: f"{obj.codigo_grupo}"
        self.fields['linea_id'].label_from_instance = lambda obj: f"{obj.codigo_linea}"
        self.fields['sublinea_id'].label_from_instance = lambda obj: f"{obj.codigo_sublinea}"
        self.fields['empresa_Id'].label_from_instance = lambda obj: f"{obj.razon_social}"
        self.fields['marca_id'].label_from_instance = lambda obj: f"{obj.codigo_marca}"
    class Meta:
        model = Articulos
        fields = [ 'codigo_sku', 'descripcion', 'factor_compra', 'factor_reparto' ]
        widgets = {
            'codigo_sku': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'factor_compra': forms.TextInput(attrs={'class': 'form-control'}),
            'factor_reparto': forms.TextInput(attrs={'class': 'form-control'}),

}
class InventarioForm(forms.ModelForm):
    empresa = forms.ModelChoiceField(
        queryset=Empresa.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    personal = forms.ModelChoiceField(
        queryset=Personal.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    sucursales = forms.ModelChoiceField(
        queryset=Sucursal.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def _init_(self, *args, **kwargs):
        super(InventarioForm, self)._init_(*args, **kwargs)

        self.fields['empresa_Id'].label_from_instance = lambda obj: f"{obj.razon_social}"
        self.fields['sucursal_id'].label_from_instance = lambda obj: f"{obj.nombre_comercial}"
    
    class Meta:
        model = Inventarios
        fields = ['nro_inventario','hora_inicio','hora_fin',
                  'total_inventario','estado','creado_por','fecha_creacion','empresa','personal']
        widgets ={
            'nro_inventario':forms.TextInput(attrs={'class':'form-control'}),
            'hora_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'total_inventario':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.TextInput(attrs={'class':'form-control'}),
            'creado_por':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_creacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'creado_por':forms.TextInput(attrs={'class':'form-control'}),
            'creado_por':forms.TextInput(attrs={'class':'form-control'}),
        }



class ItemsInventarioForm(forms.ModelForm):
    articulo = forms.ModelChoiceField(
        queryset=Articulos.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    inventario = forms.ModelChoiceField(
        queryset=Inventarios.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def _init_(self, *args, **kwargs):
        super(ItemsInventarioForm, self)._init_(*args, **kwargs)

        self.fields['item_id'].label_from_instance = lambda obj: f"{obj.codigo_sku}"
        self.fields['inventario_id'].label_from_instance = lambda obj: f"{obj.nro_inventario}"

    
    class Meta:
        model = ItemsInventario
        fields=['nro_item','stock_fisico','devoluciones_pendientes','total_unidades_stock',
                'precio_costo','total_item']
        widgets ={
            'nro_item':forms.TextInput(attrs={'class':'form-control'}),
            'stock_fisico':forms.TextInput(attrs={'class':'form-control'}),
            'devoluciones_pendientes':forms.TextInput(attrs={'class':'form-control'}),
            'total_unidades_stock':forms.TextInput(attrs={'class':'form-control'}),
            'precio_costo':forms.TextInput(attrs={'class':'form-control'}),
            'total_item':forms.TextInput(attrs={'class':'form-control'}),
        }      
class UsuarioProfileForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username','fullname', 'email' , 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'forms-control'})
        }
