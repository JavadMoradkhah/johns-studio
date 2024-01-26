# Generated by Django 4.2.9 on 2024-01-26 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactinfo',
            options={'verbose_name': 'Contact Info', 'verbose_name_plural': 'Contact Info'},
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name': 'Portfolio', 'verbose_name_plural': 'Portfolio'},
        ),
        migrations.AlterModelOptions(
            name='socialmedainfo',
            options={'verbose_name': 'Social Media Info', 'verbose_name_plural': 'Social Media Info'},
        ),
        migrations.AlterField(
            model_name='instagrampost',
            name='portfolio',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='instagram_post', serialize=False, to='core.portfolio'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='portfolio', to='core.category'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='slide',
            name='portfolio',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='slide', serialize=False, to='core.portfolio'),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]