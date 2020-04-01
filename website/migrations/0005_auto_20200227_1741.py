# Generated by Django 3.0.3 on 2020-02-27 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20200227_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='choice',
            field=models.CharField(choices=[('Pediatric', 'Pediatric'), ('Generalist', 'Generalist'), ('Ophtalmology', 'Ophtalmology'), ('Surgery', 'Surgery'), ('Cardiology', 'Cardiology')], max_length=255),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='location',
            field=models.CharField(choices=[('Alba Iulia', 'Alba Iulia'), ('Cluj-Napoca', 'Cluj-Napoca'), ('Bucharest', 'Bucharest'), ('Surgery', 'Surgery'), ('Cardiology', 'Cardiology')], max_length=255),
        ),
    ]