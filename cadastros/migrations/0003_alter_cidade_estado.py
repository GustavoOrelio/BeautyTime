# Generated by Django 4.1.7 on 2023-04-18 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_estado_alter_agendamento_dataagendamento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.estado'),
        ),
    ]
