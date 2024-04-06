# Generated by Django 5.0.2 on 2024-02-19 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_employee_data_emp_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_data',
            name='emp_id',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='employee_data',
            name='emp_role',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employee_data',
            name='emp_updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]