# Generated by Django 5.0.2 on 2024-02-19 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_employee_data_emp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_data',
            name='emp_id',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='employee_data',
            name='emp_role',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='employee_data',
            name='emp_updated_at',
            field=models.DateTimeField(),
        ),
    ]
