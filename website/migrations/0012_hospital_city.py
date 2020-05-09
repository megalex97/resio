# Generated by Django 3.0.3 on 2020-04-16 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_remove_hospital_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website.City'),
            preserve_default=False,
        ),
    ]