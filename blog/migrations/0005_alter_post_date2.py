# Generated by Django 4.2.13 on 2024-05-11 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_date2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date2',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]