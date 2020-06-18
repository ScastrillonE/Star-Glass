from django.db import models
import PIL
from PIL import Image

def serviceImageName(title):
    return 'service {}'.format(title)

# Create your models here.
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.BooleanField('activado/desactivado', default=True)


    class Meta:
        abstract= True

class Service(BaseModel):
    title=models.CharField(max_length=300, verbose_name='Titulo del servicio')
    image = models.ImageField(upload_to='services')

    class Meta():
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
       return self.title

    def save(self):
        super(Service, self).save()
        image = Image.open(self.image)
        image = image.resize((370,246), Image.ANTIALIAS)
        image.save(self.image.path)



class Project(BaseModel):
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True,
                                verbose_name='Seleccione el servicio')
    title = models.CharField(max_length=300, null=True)
    image = models.ImageField(upload_to='projects')

    class Meta():
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return self.title

    def save(self):
        super(Project, self).save()
        image = Image.open(self.image)
        image = image.resize((370,246), Image.ANTIALIAS)
        image.save(self.image.path)

class Testimonial(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    position = models.CharField(max_length=100, verbose_name='Cargo')
    content = models.TextField(max_length=800, verbose_name='Contenido')

    class Meta:
        verbose_name = 'Testimonio'
        verbose_name_plural = 'Testimonios'

    def __str__(self):
        return '{} -- {}'.format(self.name, self.content)

class PopUp(BaseModel):
    content = models.TextField()
