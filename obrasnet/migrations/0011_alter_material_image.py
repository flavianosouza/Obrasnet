# Generated by Django 4.0.10 on 2023-05-17 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obrasnet', '0010_alter_material_advantage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='image',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
