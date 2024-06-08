# Generated by Django 4.0.6 on 2024-04-17 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='ano_de_lancamento',
            new_name='ano_lancamento',
        ),
        migrations.RenameField(
            model_name='banda',
            old_name='ano_de_formacao',
            new_name='ano_criacao',
        ),
        migrations.AddField(
            model_name='banda',
            name='nacionalidade',
            field=models.CharField(default='Desconhecida', max_length=50),
        ),
    ]
