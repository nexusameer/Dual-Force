# Generated by Django 5.0.6 on 2024-06-25 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_alter_testimonals_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonals',
            name='image',
            field=models.FileField(default='images/user.jpg', upload_to='media/Testimonals'),
        ),
    ]
