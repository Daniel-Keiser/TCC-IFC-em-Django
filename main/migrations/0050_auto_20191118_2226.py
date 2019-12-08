# Generated by Django 2.2.4 on 2019-11-19 01:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0049_auto_20191118_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='almossom',
            name='bandas',
            field=models.ManyToManyField(related_name='bandas', through='main.ProgramacaoAlmossom', to='main.Banda'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(default='self.user.username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='programacaoalmossom',
            name='banda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Banda'),
        ),
    ]
