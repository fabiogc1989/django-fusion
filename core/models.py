import uuid
from django.db import models

from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    uuid4_filename = f'{uuid.uuid4()}'
    return f'{uuid4_filename}.{ext}'


class Base(models.Model):
    createdOn = models.DateField('Criação', auto_now_add = True)
    modifiedOn = models.DateField('Modificação', auto_now = True)
    active = models.BooleanField('Ativo?', default = True)

    class Meta:
        abstract = True


class Service(Base):
    ICON_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Utilizadores'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete')
    )

    name = models.CharField('Serviço', max_length = 100)
    description = models.TextField('Descrição', max_length = 200)
    icon = models.CharField('Icone', max_length = 12, choices = ICON_CHOICES)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
    
    def __str__(self):
        return self.name


class Position(Base):
    name = models.CharField('Cargo', max_length = 100)

    class Meta:
         verbose_name = 'Position'
         verbose_name_plural = 'Positions'
    
    def __str__(self):
        return self.name


class Employee(Base):
    name = models.CharField('Nome', max_length = 100)
    position = models.ForeignKey('core.Position', verbose_name = 'Position', on_delete = models.CASCADE)
    biography = models.TextField('Biografia', max_length = 200)
    image = StdImageField('Imagem', upload_to = get_file_path, variations = {'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length = 100, default = '#')
    twitter = models.CharField('Twitter', max_length = 100, default = '#')
    Instagram = models.CharField('Instagram', max_length = 100, default = '#')

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
    
    def __str__(self):
        return self.name
