# Generated by Django 2.1.1 on 2018-10-22 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20181022_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment_comment_like',
            name='comment_comment',
        ),
        migrations.RemoveField(
            model_name='comment_comment_like',
            name='user',
        ),
        migrations.DeleteModel(
            name='comment_comment_like',
        ),
    ]
