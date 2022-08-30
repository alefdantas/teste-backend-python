# Generated by Django 4.1 on 2022-08-26 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loss_comunication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produtor', models.CharField(max_length=75)),
                ('email_produtor', models.EmailField(max_length=254)),
                ('cpf_produtor', models.CharField(max_length=11)),
                ('latitude_produtor', models.CharField(max_length=200)),
                ('longitude_produtor', models.CharField(max_length=200)),
                ('tipo_lavoura_produtor', models.CharField(max_length=75)),
                ('data_colheita_produtor', models.DateTimeField()),
                ('evento_ocorrido_produtor', models.CharField(max_length=75)),
            ],
        ),
    ]