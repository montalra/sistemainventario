from django.contrib import admin
from.models import Empresa,Sucursal,Personal,GruposProveedor,ItemsInventario,Inventarios
# Register your models here.

admin.site.register(Empresa)
admin.site.register(Personal)
admin.site.register(Sucursal)
admin.site.register(GruposProveedor)
admin.site.register(Inventarios)
admin.site.register(ItemsInventario)
