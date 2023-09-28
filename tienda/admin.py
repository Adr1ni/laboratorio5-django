from django.contrib import admin
from .models import *
from django.db.models import Count

def actualizar_estado_agotado(modeladmin, request, queryset):
    queryset.update(stock=0)
actualizar_estado_agotado.short_description = "Actualizar estado a Agotado"



class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'pub_date')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'categoria__nombre')  
    actions = [actualizar_estado_agotado]



class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pub_date')
    
    def productos_en_categoria(self, obj):
        return obj.producto_set.count()
    productos_en_categoria.short_description = 'Productos en esta categoría'
    
    def productos_chart_data(self, obj):
        data = []
        categorias = Categoria.objects.annotate(total_productos=Count('producto'))
        for categoria in categorias:
            data.append({'name': categoria.nombre, 'value': categoria.total_productos})
        return data
    productos_chart_data.short_description = 'Gráfico de productos por categoría'


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'dni', 'telefono', 'direccion', 'email', 'fecha_de_nacimiento')


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)

