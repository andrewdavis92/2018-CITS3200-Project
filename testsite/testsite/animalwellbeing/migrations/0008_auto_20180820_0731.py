# Generated by Django 2.1 on 2018-08-20 07:31

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('animalwellbeing', '0007_coversheetform_all_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coversheetform',
            name='all_data',
            field=picklefield.fields.PickledObjectField(blank=True, editable=False),
        ),
    ]
