from django.db import models

class Pan(models.Model):

    codigo              = models.IntegerField()
    nombre              = models.CharField(max_length=20)
    precio              = models.IntegerField()
    descripcion         = models.CharField(max_length=20)
    imagen              = models.ImageField(upload_to="productos", null=True)  

    def __str__(self):
        return self.nombre 
    
    @property
    def imagen_url(self):
        if self.imagen:
            return self.imagen.url
        else:
            return ''




