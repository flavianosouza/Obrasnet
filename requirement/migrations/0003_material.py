# Generated by Django 4.2.1 on 2023-05-19 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('requirement', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('image', models.TextField(null=True)),
                ('specification', models.TextField(null=True)),
                ('ref', models.CharField(db_index=True, max_length=30, null=True)),
                ('price', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('advantage', models.TextField(max_length=255, null=True)),
                ('documentation', models.TextField(null=True)),
                ('features', models.TextField(null=True)),
                ('url', models.URLField()),
                ('state', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='requirement.category')),
            ],
        ),
    ]