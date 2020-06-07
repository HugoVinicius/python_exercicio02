# Generated by Django 3.0.6 on 2020-05-06 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('idade', models.IntegerField(default=0)),
                ('data_nascimento', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=200)),
                ('numero', models.IntegerField()),
                ('cep', models.CharField(max_length=9)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Pessoa')),
            ],
        ),
    ]
