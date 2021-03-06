# Generated by Django 3.2.9 on 2022-02-21 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cooperante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cooperante', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Nombre del cooperante',
            },
        ),
        migrations.CreateModel(
            name='Eje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_eje', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Nombre del eje',
            },
        ),
        migrations.CreateModel(
            name='LugarEjecicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_lugar', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Lugar de ejecucion',
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('imagen_principal', models.ImageField(upload_to='noticias_imagenes')),
                ('galeria', models.FileField(upload_to='galeria/')),
                ('avances_proyecto', models.IntegerField(choices=[(0, ''), (1, 'Iniciado'), (2, 'En progreso'), (3, 'Finalizado')], default=0)),
                ('status', models.IntegerField(choices=[(0, 'Publicado'), (1, 'Ocultar')], default=0)),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('cooperante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coperante', to='ejeproyectos.cooperante')),
                ('eje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eje', to='ejeproyectos.eje')),
                ('lugar_ejecucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ejecucion', to='ejeproyectos.lugarejecicion')),
            ],
            options={
                'verbose_name': 'Publicaci??n de proyectos',
            },
        ),
    ]
