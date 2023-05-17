# Generated by Django 4.2.1 on 2023-05-12 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0003_alter_empresa_name'),
        ('departamentos', '0003_departamentos_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamentos',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='empresas.empresa'),
            preserve_default=False,
        ),
    ]
