# Generated by Django 4.0.5 on 2022-07-19 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0006_taskcontroll_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcontroll',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.task'),
        ),
    ]
