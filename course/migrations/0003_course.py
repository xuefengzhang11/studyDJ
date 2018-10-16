# Generated by Django 2.1.1 on 2018-09-29 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_degree'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('introduce', models.CharField(max_length=255)),
                ('price', models.FloatField(default=0.0)),
                ('imgurl', models.CharField(max_length=100)),
                ('cs_categry', models.ForeignKey(on_delete=True, to='course.category')),
                ('cs_degree', models.ForeignKey(on_delete=True, to='course.degree')),
                ('cs_direction', models.ForeignKey(on_delete=True, to='course.direction')),
            ],
        ),
    ]