# Generated by Django 3.0 on 2020-01-15 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GameFaqs_Backend', '0008_auto_20200115_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='the_question',
        ),
    ]
