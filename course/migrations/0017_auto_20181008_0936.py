# Generated by Django 2.1.1 on 2018-10-08 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0016_auto_20181008_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='cs_career',
            field=models.ForeignKey(null=True, on_delete=True, to='career.career'),
        ),
        migrations.AlterField(
            model_name='course',
            name='cs_category',
            field=models.ForeignKey(on_delete=True, to='course.category'),
        ),
    ]