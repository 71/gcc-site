# Generated by Django 2.2.10 on 2020-03-16 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('gcc', '0008_event_is_long')]

    operations = [
        migrations.AddField(
            model_name='edition',
            name='long_description',
            field=models.TextField(default=''),
        )
    ]