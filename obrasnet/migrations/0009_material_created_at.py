# Generated by Django 4.0.10 on 2023-05-17 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obrasnet', '0008_category_sheetname'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
