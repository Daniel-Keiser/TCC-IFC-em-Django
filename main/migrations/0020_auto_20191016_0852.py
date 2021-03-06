# Generated by Django 2.2.4 on 2019-10-16 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20191016_0840'),
    ]

    operations = [
        migrations.AddField(
            model_name='almossom',
            name='descricao',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='almossom',
            name='bandas',
            field=models.ManyToManyField(through='main.ProgramacaoAlmossom', to='main.Banda'),
        ),
        migrations.AlterField(
            model_name='programacaoalmossom',
            name='banda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Banda'),
        ),
    ]
