# Generated by Django 3.1.7 on 2021-05-25 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='adress',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='emails',
            new_name='email',
        ),
    ]
