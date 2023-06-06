# Generated by Django 4.1.2 on 2023-06-06 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(db_column='IdCategory', primary_key=True, serialize=False)),
                ('nom_category', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Form_contact',
            fields=[
                ('id_form_cont', models.IntegerField(db_column='Id_form_cont', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('fono', models.IntegerField()),
                ('decripcion', models.CharField(max_length=120)),
                ('titulo', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Parti',
            fields=[
                ('id_tp_part', models.AutoField(db_column='IdTipo_Part', primary_key=True, serialize=False)),
                ('tipo_part', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Parti',
            fields=[
                ('id_parti', models.IntegerField(db_column='Id_Parti', primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=30)),
                ('Apellido', models.CharField(max_length=30)),
                ('Rut', models.IntegerField()),
                ('dv', models.CharField(max_length=1)),
                ('correo', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('fono', models.IntegerField()),
                ('id_tp_part', models.ForeignKey(db_column='IdTipo_Part', on_delete=django.db.models.deletion.CASCADE, to='noticias.tipo_parti')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id_noticia', models.IntegerField(db_column='Id_Noticia', primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('titulo', models.CharField(max_length=35)),
                ('Detalle', models.CharField(max_length=120)),
                ('Ubicacion', models.CharField(max_length=120)),
                ('id_categoria', models.ForeignKey(db_column='IdCategory', on_delete=django.db.models.deletion.CASCADE, to='noticias.categoria')),
                ('id_parti', models.ForeignKey(db_column='Id_Parti', on_delete=django.db.models.deletion.CASCADE, to='noticias.parti')),
            ],
        ),
    ]
