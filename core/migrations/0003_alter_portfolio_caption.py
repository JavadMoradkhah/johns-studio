# Generated by Django 4.2.9 on 2024-01-26 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_contactinfo_options_alter_portfolio_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='caption',
            field=models.CharField(max_length=255),
        ),
    ]
