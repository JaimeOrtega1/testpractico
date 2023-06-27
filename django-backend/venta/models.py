from django.db import models
from inventario.models import *
# Create your models here.

class Cliente (models.Model):
    codigo = models.CharField(max_length=100,blank=True,null=True)
    nombre = models.CharField(max_length=100,blank=True,null=True)
    telefono = models.CharField(max_length=20,blank=True,null=True)
    direccion = models.CharField(max_length=1024,blank=True,null=True)
    email = models.CharField(max_length=100,blank=True,null=True)
    estado = models.CharField(max_length=100,blank=True,null=True)

    #Metadata
    class Meta :
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['-nombre']

    def __str__(self):
        return self.nombre

class TipoPago (models.Model):
    codigo = models.CharField(max_length=20, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    estado = models.BooleanField(default=True)

    class Meta :
        ordering = ['-nombre']

    def __str__(self):
        return self.nombre

class Venta (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
    tipo_pago = models.ForeignKey(TipoPago, on_delete=models.CASCADE, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    impuesto = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    estado = models.BooleanField(default=True)

   #Metadata
    class Meta :
       verbose_name = 'Venta'
       verbose_name_plural = 'Ventas'
       ordering = ['-numero']

    def __str__(self):
       return self.numero

class VentaDetalle (models.Model):
   venta = models.ForeignKey(Venta, on_delete=models.CASCADE, blank=True, null=True)
   producto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True, null=True)
   precio = models.DecimalField(max_digits=8, decimal_places=2, default=0, blank=True, null=True)
   cantidad = models.DecimalField(max_digits=8, decimal_places=2, default=0, blank=True, null=True)
   subtotal = models.DecimalField(max_digits=8, decimal_places=2, default=0, blank=True, null=True)
   impuesto = models.DecimalField(max_digits=8, decimal_places=2, default=0, blank=True, null=True)
   total = models.DecimalField(max_digits=8, decimal_places=2, default=0, blank=True, null=True)

   #Metadata
   class Meta :
       verbose_name = 'Venta Detalle'
       verbose_name_plural = 'Ventas Detalle'
       ordering = ['-numero']


   def __str__(self):
       return self.producto
