# Generated by Django 3.1 on 2020-10-05 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_reportimage_datauri'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportimage',
            name='picture',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]