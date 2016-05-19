# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-12 21:30
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
        ),
        migrations.CreateModel(
            name='beneficiario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('apellido', models.CharField(max_length=70)),
                ('numero_documento', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=70)),
                ('genero', models.CharField(choices=[('M', 'masculino'), ('F', 'femenino')], max_length=1)),
                ('fecha_de_nacimiento', models.DateField()),
                ('eps', models.CharField(max_length=70)),
                ('barrio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajo_final.Barrio')),
            ],
            options={
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
        ),
        migrations.CreateModel(
            name='entidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('documento', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=30)),
                ('sexo', models.CharField(choices=[('M', 'masculino'), ('F', 'femenino')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='tipoDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
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
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajo_final.tipoDocumento'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='programa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajo_final.programa'),
        ),
        migrations.AddField(
            model_name='barrio',
            name='comuna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajo_final.Comuna'),
        ),
    ]
