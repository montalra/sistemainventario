from django.db import models
import uuid

class Empresa(models.Model):
    empresa_Id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    nro_documento = models.CharField(max_length=11)
    razon_social = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)

    class Meta:
        db_table = 'empresa'

    def __str__(self):
        return self.razon_social

class Sucursal(models.Model):
    sucursal_id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    empresa_Id = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True)
    nombre_comercial = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)

    class Meta:
        db_table = 'sucursal'

    def __str__(self):
        return self.nombre_comercial

class Personal(models.Model):
    personal_id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    nombre_personal = models.CharField(max_length=100)
    direccion_personal = models.CharField(max_length=150)
    tipo_documento = models.CharField(max_length=1)
    nro_documento = models.CharField(max_length=11)
    empresa_Id = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'personal'

    def __str__(self):
        return self.nombre_personal

class GruposProveedor(models.Model):
    grupo_id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    codigo_grupo = models.CharField(max_length=15)
    grupo_descripcion = models.CharField(max_length=100)
    empresa_Id = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True )
    activo = models.BooleanField(default=True)
    responsable_grupo = models.ForeignKey(Personal, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'grupos_proveedor'

    def __str__(self):
        return self.grupo_descripcion

class UnidadesMedida(models.Model):
    unidad_medida_id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    unidad_nombre = models.CharField(max_length=150)

    class Meta:
        db_table = 'unidades_medida'

    def __str__(self):
        return self.unidad_nombre

class LineasArticulos(models.Model):
    linea_id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    codigo_linea = models.CharField(max_length=15)
    linea_descripcion = models.CharField(max_length=100)
    grupo_id = models.ForeignKey(GruposProveedor, on_delete=models.CASCADE, null=True)
    activo = models.BooleanField(default=True)
    responsable_linea = models.ForeignKey(Personal, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        db_table = 'lineas_articulos'

    def __str__(self):
        return self.linea_descripcion

class SublineasArticulos(models.Model):
    sublinea_id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    codigo_sublinea = models.CharField(max_length=15)
    sublinea_descripcion = models.CharField(max_length=100)
    linea_id = models.ForeignKey(LineasArticulos, on_delete=models.CASCADE, null=True)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'sublineas_articulos'

    def __str__(self):
        return self.sublinea_descripcion

class Marcas(models.Model):
    marca_id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    codigo_marca = models.CharField(max_length=14)
    marca_nombre = models.CharField(max_length=150)

    class Meta:
        db_table = 'marcas'

    def __str__(self):
        return self.marca_nombre

class Articulos(models.Model):
    articulo_id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    codigo_sku = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=150)
    unidad_medida_id = models.ForeignKey(UnidadesMedida, on_delete=models.CASCADE , null=True)
    grupo_id = models.ForeignKey(GruposProveedor, on_delete=models.CASCADE , null=True)
    linea_id = models.ForeignKey(LineasArticulos, on_delete=models.CASCADE,  null=True)
    sublinea_id = models.ForeignKey(SublineasArticulos, on_delete=models.CASCADE,null=True)
    empresa_Id = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True)
    factor_compra = models.PositiveIntegerField()
    factor_reparto = models.PositiveIntegerField()
    marca_id = models.ForeignKey(Marcas, on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'articulos'

    def __str__(self):
        return self.descripcion

class Inventarios(models.Model):
    inventario_id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    empresa_Id = models.ForeignKey(Empresa, on_delete=models.CASCADE,null=True)
    sucursal_id = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True)
    fecha_inventario = models.DateTimeField(auto_now_add=True)
    nro_inventario = models.PositiveIntegerField()
    responsable = models.ForeignKey(Personal, on_delete=models.CASCADE, null=True)
    hora_inicio = models.DateTimeField()
    hora_fin = models.DateTimeField()
    total_inventario = models.DecimalField(max_digits=12, decimal_places=2)
    estado = models.PositiveIntegerField()
    creado_por = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField()

    class Meta:
        db_table = 'inventarios'

    def __str__(self):
        return str(self.nro_inventario)

class ItemsInventario(models.Model):
    item_id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    inventario_id = models.ForeignKey(Inventarios, on_delete=models.CASCADE, null=True)
    nro_item = models.PositiveIntegerField()
    articulo_id = models.ForeignKey(Articulos, on_delete=models.CASCADE, null=True)
    stock_fisico = models.DecimalField(max_digits=12, decimal_places=2)
    devoluciones_pendientes = models.DecimalField(max_digits=12, decimal_places=2)
    total_unidades_stock = models.DecimalField(max_digits=12, decimal_places=2)
    precio_costo = models.DecimalField(max_digits=12, decimal_places=2)
    total_item = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = 'items_inventario'

    def __str__(self):
        return f'Item {self.nro_item} - {self.articulo_id.descripcion}'

class Usuario(models.Model):
    username = models.CharField(max_length=50,)
    email = models.EmailField(unique = True)
    fullname = models.CharField(max_length=100,null=False)
    password = models.CharField(max_length=150, null=True)
    
    class Meta:
        db_table = 'usuario'
    
    def __str__ (self):
        return self.email