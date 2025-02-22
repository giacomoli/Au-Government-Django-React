# Generated by Django 2.0 on 2018-07-17 15:34

import accounts.managers
import sitename.mixins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('second_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('rate', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='users/photos')),
                ('mobile', models.CharField(blank=True, max_length=30, null=True)),
                ('admission_date', models.DateField(auto_now_add=True, null=True)),
                ('salutation', models.IntegerField(choices=[(1, 'Mr'), (2, 'Mrs'), (3, 'Ms'), (4, 'Miss'), (5, 'Dr')], default=1)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, sitename.mixins.UpdateAttributesMixin),
            managers=[
                ('objects', accounts.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('organisation__name', 'contact__first_name', 'contact__last_name'),
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=256)),
                ('last_name', models.CharField(blank=True, max_length=256)),
                ('middle_name', models.CharField(blank=True, max_length=256, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('secondary_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('mobile', models.CharField(blank=True, max_length=256, null=True)),
                ('salutation', models.IntegerField(choices=[(1, 'Mr'), (2, 'Mrs'), (3, 'Ms'), (4, 'Miss'), (5, 'Dr')], null=True)),
                ('skype', models.CharField(blank=True, max_length=25, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('preferred_first_name', models.CharField(blank=True, max_length=256, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True)),
                ('estimated_wealth', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('estimated_wealth_date', models.DateField(blank=True, null=True)),
                ('voi', models.BooleanField(default=False)),
                ('direct_line', models.CharField(blank=True, max_length=100, null=True)),
                ('beverage', models.CharField(blank=True, max_length=25, null=True)),
                ('role', models.CharField(blank=True, max_length=100, null=True)),
                ('is_general', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('first_name', 'last_name'),
            },
            bases=(models.Model, sitename.mixins.UpdateAttributesMixin),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(blank=True, max_length=256, null=True)),
                ('address2', models.CharField(blank=True, max_length=256, null=True)),
                ('suburb', models.CharField(blank=True, max_length=256, null=True)),
                ('state', models.IntegerField(blank=True, choices=[(1, 'SA'), (2, 'NSW'), (3, 'VIC'), (4, 'WA'), (5, 'QLD'), (6, 'TAS'), (7, 'NT'), (8, 'ACT')], null=True)),
                ('post_code', models.CharField(blank=True, max_length=15, null=True)),
                ('country', models.CharField(blank=True, max_length=256, null=True)),
            ],
            bases=(models.Model, sitename.mixins.UpdateAttributesMixin),
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('main_line', models.CharField(blank=True, max_length=30, null=True)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('group_status', models.IntegerField(choices=[(1, 'Parent'), (2, 'Group memeber')])),
                ('business_search_words', models.TextField(blank=True, null=True)),
                ('group_parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_children', to='accounts.Organisation')),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model, sitename.mixins.UpdateAttributesMixin),
        ),
    ]
