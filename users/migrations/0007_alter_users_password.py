# Generated by Django 4.2.9 on 2024-01-07 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_users_groups_alter_users_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
