# Generated by Django 3.1.7 on 2021-05-12 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20210505_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viewer',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='manager',
        ),
        migrations.DeleteModel(
            name='user',
        ),
        migrations.DeleteModel(
            name='viewer',
        ),
    ]
