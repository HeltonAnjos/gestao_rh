# Generated by Django 4.2.1 on 2023-05-29 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0004_alter_registrohoraextra_motivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrohoraextra',
            name='horas',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]
