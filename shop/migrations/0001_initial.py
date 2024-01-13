# Generated by Django 5.0.1 on 2024-01-11 18:55

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Praduct',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('praduct_image', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(default=0.0)),
                ('existence', models.BooleanField(default=False)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='shop.category')),
            ],
        ),
    ]
