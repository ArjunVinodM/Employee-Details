# Generated by Django 4.1 on 2022-08-18 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp_app.department'),
        ),
    ]
