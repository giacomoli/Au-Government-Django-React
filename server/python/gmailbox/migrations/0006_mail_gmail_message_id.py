# Generated by Django 2.0 on 2018-09-12 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gmailbox', '0005_auto_20180912_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='gmail_message_id',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
