# Generated by Django 2.1.1 on 2018-10-23 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0040_auto_20181023_1313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sectioncomment_like',
            old_name='section',
            new_name='sectioncomment',
        ),
        migrations.AlterField(
            model_name='course',
            name='cs_category',
            field=models.ForeignKey(on_delete=True, to='course.category'),
        ),
    ]
