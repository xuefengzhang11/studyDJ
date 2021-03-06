# Generated by Django 2.1.1 on 2018-10-23 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20181022_1833'),
        ('course', '0038_auto_20181023_0853'),
    ]

    operations = [
        migrations.CreateModel(
            name='sectioncomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('uptime', models.DateTimeField(auto_now_add=True)),
                ('like', models.IntegerField(default=0)),
                ('section', models.ForeignKey(on_delete=True, to='course.section')),
                ('user', models.ForeignKey(on_delete=True, to='user.userdetail')),
            ],
        ),
        migrations.CreateModel(
            name='sectioncomment_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('uptime', models.DateTimeField(auto_now_add=True)),
                ('like', models.IntegerField(default=0)),
                ('sectioncomment', models.ForeignKey(on_delete=True, to='course.sectioncomment')),
                ('user', models.ForeignKey(on_delete=True, to='user.userdetail')),
            ],
        ),
        migrations.CreateModel(
            name='sectioncomment_comment_like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sectioncomment_comment', models.ForeignKey(on_delete=True, to='course.sectioncomment_comment')),
                ('user', models.ForeignKey(on_delete=True, to='user.userdetail')),
            ],
        ),
        migrations.CreateModel(
            name='sectioncomment_like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.ForeignKey(on_delete=True, to='course.section')),
                ('user', models.ForeignKey(on_delete=True, to='user.userdetail')),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='cs_category',
            field=models.ForeignKey(on_delete=True, to='course.category'),
        ),
    ]
