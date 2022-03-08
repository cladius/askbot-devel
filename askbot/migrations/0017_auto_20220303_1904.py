# Generated by Django 2.2.27 on 2022-03-03 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askbot', '0016_postrevision_ip_addr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='status',
            field=models.CharField(choices=[('d', 'administrator'), ('m', 'moderator'), ('a', 'approved'), ('w', 'watched'), ('s', 'suspended'), ('b', 'blocked'), ('t', 'terminated')], db_index=True, default='w', max_length=2),
        ),
    ]
