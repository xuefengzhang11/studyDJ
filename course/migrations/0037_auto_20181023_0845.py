# Generated by Django 2.1.1 on 2018-10-23 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0036_auto_20181022_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='cs_category',
            field=models.ForeignKey(on_delete=True, to='course.category'),
        ),
    ]
