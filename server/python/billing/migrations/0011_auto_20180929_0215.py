# Generated by Django 2.0 on 2018-09-28 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0010_auto_20180928_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalmatter',
            name='closed_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalmatter',
            name='conflict_parties',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalmatter',
            name='lead_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='matter',
            name='assistant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assistant_of_matters', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='matter',
            name='closed_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='matter',
            name='conflict_parties',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='matter',
            name='lead_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='matter',
            name='matter_sub_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matters', to='core.MatterSubType'),
        ),
    ]
