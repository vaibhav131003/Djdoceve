# Generated by Django 4.1.6 on 2023-07-04 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doceveapp', '0002_collegeevent_eventregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('docid', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('teacherid', models.CharField(default='', max_length=70)),
                ('courseid', models.CharField(default='', max_length=70)),
                ('doctype', models.CharField(default='', max_length=70)),
                ('docname', models.CharField(default='', max_length=150)),
                ('uploadby', models.CharField(default='', max_length=150)),
                ('uploadtime', models.CharField(default='', max_length=70)),
                ('uploaddate', models.CharField(default='', max_length=70)),
                ('url', models.CharField(default='', max_length=150)),
                ('remarks', models.CharField(default='', max_length=150)),
            ],
        ),
    ]
