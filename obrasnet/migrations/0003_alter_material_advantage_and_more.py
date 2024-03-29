# Generated by Django 4.0.10 on 2023-05-17 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obrasnet', '0002_material_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='advantage',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='documentation',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='features',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='price',
            field=models.JSONField(db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='ref',
            field=models.CharField(db_index=True, max_length=30, null=True),
        ),
    ]
