# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-25 04:45
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
            options={
                'db_table': 'Barrio',
            },
        ),
        migrations.CreateModel(
            name='Beneficiario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('numero_documento', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=50)),
                ('genero', models.CharField(choices=[('M', 'masculino'), ('F', 'femenino')], max_length=1)),
                ('fecha_registro', models.DateField()),
                ('hora_registro', models.TimeField()),
                ('fecha_de_nacimiento', models.DateField()),
                ('barrio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajo_final.Barrio')),
            ],
            options={
                'db_table': 'Beneficiario',
                'verbose_name': 'beneficiario',
                'verbose_name_plural': 'beneficiarios',
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
            options={
                'db_table': 'Comuna',
            },
        ),
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Entidad',
            },
        ),
        migrations.CreateModel(
            name='Eps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Eps',
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('documento', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=30)),
                ('sexo', models.CharField(choices=[('M', 'masculino'), ('F', 'femenino')], max_length=1)),
            ],
            options={
                'db_table': 'Funcionario',
            },
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'db_table': 'Programa',
            },
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'TipoDocumento',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='documento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='trabajo_final.TipoDocumento'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='eps',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='trabajo_final.Eps'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='programa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='trabajo_final.Programa'),
        ),
        migrations.AddField(
            model_name='barrio',
            name='comuna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='trabajo_final.Comuna'),
        ),
    ]
