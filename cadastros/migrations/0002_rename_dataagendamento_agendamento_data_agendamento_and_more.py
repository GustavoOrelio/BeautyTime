# Generated by Django 4.1.7 on 2023-09-11 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agendamento',
            old_name='dataAgendamento',
            new_name='data_agendamento',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='funcionario',
        ),
        migrations.AddField(
            model_name='empresa',
            name='funcionario',
            field=models.ManyToManyField(to='cadastros.funcionario'),
        ),
    ]
