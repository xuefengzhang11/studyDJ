# Generated by Django 2.1.1 on 2018-10-19 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0025_auto_20181018_1409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='course',
            new_name='section',
        ),
        migrations.RenameField(
            model_name='history',
            old_name='course',
            new_name='section',
        ),
        migrations.AlterField(
            model_name='course',
            name='cs_category',
            field=models.ForeignKey(on_delete=True, to='course.category'),
        ),
    ]
