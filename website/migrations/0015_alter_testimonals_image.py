# Generated by Django 5.0.6 on 2024-06-25 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_alter_testimonals_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonals',
            name='image',
            field=models.FileField(default='user.jpg', upload_to='media/Testimonals'),
        ),
    ]
