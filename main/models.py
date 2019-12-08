from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='static/profile_pics', default='static/images/perfil.png')
    descricao = models.CharField(blank=True, max_length=256, default='Escreva Aqui Algo Sobre Você')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    data = models.DateField()
    descricao = models.CharField(max_length=256)
    image = models.ImageField(blank=True, upload_to='static/events_pics')

    def __str__(self):
        return self.titulo

    
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 800 or img.width > 500:
            output_size = (800, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Instrumento(models.Model):
    nome = models.CharField(max_length=100)

class Banda(models.Model):
    nome = models.CharField(max_length=100, null=False)
    descricao = models.CharField(max_length=256)
    lider = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "<" + self.nome + " - " + self.descricao + ">"
    
    

class Almossom(models.Model):
    data = models.DateTimeField()
    bandas = models.ManyToManyField(Banda, through="ProgramacaoAlmossom")
    image = models.ImageField(blank=True, upload_to='static/almosom_pics')
    info = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=256)
    bandas = models.ManyToManyField(Banda, through='ProgramacaoAlmossom', related_name='bandas')


    def __str__(self):
        return self.descricao

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 800 or img.width > 500:
            output_size = (800, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)



class ProgramacaoAlmossom(models.Model):
    banda =  models.ForeignKey(Banda, on_delete=models.CASCADE)
    almossom =  models.ForeignKey(Almossom, on_delete=models.CASCADE)

    def __str__(self):
        return "<" + self.almossom.descricao + " - " + self.banda.nome + ">"

class Galeria(models.Model):

    image = models.ImageField(blank=True, upload_to='static/galeria')

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 800 or img.width > 600:
            output_size = (600, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)