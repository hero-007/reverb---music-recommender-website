# Generated by Django 2.0.4 on 2018-04-27 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0002_user_ids'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_Ids',
            new_name='User_Id',
        ),
    ]
