# Generated by Django 3.2.5 on 2022-03-12 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_investor_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='investor',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]