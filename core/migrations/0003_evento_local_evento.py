# Generated by Django 5.0.6 on 2024-07-02 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_evento_usuario_alter_evento_data_criacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='local_evento',
            field=models.CharField(default=1, max_length=100, verbose_name='Local do evento'),
            preserve_default=False,
        ),
    ]
