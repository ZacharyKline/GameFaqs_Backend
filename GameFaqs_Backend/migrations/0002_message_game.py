# Generated by Django 3.0 on 2020-01-03 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GameFaqs_Backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gameify', to='GameFaqs_Backend.Game'),
        ),
    ]
