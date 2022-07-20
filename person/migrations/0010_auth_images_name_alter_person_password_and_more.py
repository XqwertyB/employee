# Generated by Django 4.0.5 on 2022-07-20 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0009_remove_taskcontroll_emp_count_taskcontroll_emp_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username1', models.CharField(max_length=100)),
                ('password1', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='images',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='username',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='taskcontroll',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Tugatilgan'),
        ),
        migrations.AlterField(
            model_name='taskcontroll',
            name='status_task',
            field=models.BooleanField(default=False, verbose_name='Uz vaqtida tugatilgan'),
        ),
    ]
