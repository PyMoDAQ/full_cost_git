# Generated by Django 2.2.8 on 2020-02-14 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imag', '0007_auto_20200122_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalrecord',
            name='billing',
            field=models.CharField(choices=[('SPECTRO', 'Optical Spectroscopy'), ('TEM', 'Electronic Microscopy'), ('PREPA', 'Sample Preparation'), ('MEBA', 'Advanced MEB'), ('FIBCR', 'FIB Clean Room'), ('SOFT', 'Soft Matter'), ('MATCARAC', 'PS2I'), ('MAGNETIC', 'Magnetic Measurement'), ('CHEM', 'Chemistry'), ('CLEANR', 'Clean Room Processes'), ('UHVI', 'UHV Imagery'), ('LT4', 'LT-UHV 4 tips'), ('DUFG', 'Growth DUF'), ('NEARF', 'Near-field microscopy'), ('GROWTHIMP', 'Growth and Implantation'), ('MECA', 'Mechanic Service'), ('ELEC', 'Electronic Service')], default='SPECTRO', max_length=200),
        ),
        migrations.AlterField(
            model_name='record',
            name='billing',
            field=models.CharField(choices=[('SPECTRO', 'Optical Spectroscopy'), ('TEM', 'Electronic Microscopy'), ('PREPA', 'Sample Preparation'), ('MEBA', 'Advanced MEB'), ('FIBCR', 'FIB Clean Room'), ('SOFT', 'Soft Matter'), ('MATCARAC', 'PS2I'), ('MAGNETIC', 'Magnetic Measurement'), ('CHEM', 'Chemistry'), ('CLEANR', 'Clean Room Processes'), ('UHVI', 'UHV Imagery'), ('LT4', 'LT-UHV 4 tips'), ('DUFG', 'Growth DUF'), ('NEARF', 'Near-field microscopy'), ('GROWTHIMP', 'Growth and Implantation'), ('MECA', 'Mechanic Service'), ('ELEC', 'Electronic Service')], default='SPECTRO', max_length=200),
        ),
    ]
