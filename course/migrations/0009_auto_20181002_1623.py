# Generated by Django 2.1.1 on 2018-10-02 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_auto_20181002_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('introduce', models.CharField(max_length=255)),
                ('upload', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='cs_category',
            field=models.ForeignKey(on_delete=True, to='course.category'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(on_delete=True, to='course.course'),
        ),
    ]
