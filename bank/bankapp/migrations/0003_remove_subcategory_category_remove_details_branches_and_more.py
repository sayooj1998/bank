# Generated by Django 4.1.5 on 2023-07-18 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_category_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='details',
            name='branches',
        ),
        migrations.RemoveField(
            model_name='details',
            name='district',
        ),
        migrations.RemoveField(
            model_name='details',
            name='material',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
    ]