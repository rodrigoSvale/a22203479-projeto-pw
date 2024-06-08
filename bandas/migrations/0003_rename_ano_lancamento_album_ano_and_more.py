# Generated by Django 4.0.6 on 2024-04-17 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0002_rename_ano_de_lancamento_album_ano_lancamento_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='ano_lancamento',
            new_name='ano',
        ),
        migrations.RenameField(
            model_name='banda',
            old_name='ano_criacao',
            new_name='ano',
        ),
        migrations.RenameField(
            model_name='musica',
            old_name='link_spotify',
            new_name='spotify_link',
        ),
        migrations.AlterField(
            model_name='banda',
            name='nacionalidade',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='musica',
            name='duracao',
            field=models.CharField(max_length=100),
        ),
    ]
