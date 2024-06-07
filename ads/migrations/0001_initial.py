# Generated by Django 5.0.6 on 2024-06-05 08:38

import ads.models
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.CharField(default=ads.models.id_generator, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.CharField(default=ads.models.id_generator, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='default_user_photo.jpg', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'heic', 'img'])])),
                ('subject', models.CharField(max_length=150)),
                ('publish_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('bought', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=3, default=0, max_digits=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.category')),
            ],
            options={
                'ordering': ['-publish_time'],
            },
        ),
    ]