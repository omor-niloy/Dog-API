# Generated by Django 4.2 on 2023-04-08 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogapp', '0005_breed_alter_dog_breed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Breed',
        ),
    ]