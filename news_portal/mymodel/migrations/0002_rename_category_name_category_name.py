# Generated by Django 4.2.13 on 2024-06-08 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mymodel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name',
        ),
    ]