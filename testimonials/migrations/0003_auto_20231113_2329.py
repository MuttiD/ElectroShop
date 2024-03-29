# Generated by Django 3.2 on 2023-11-13 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0002_testimonial_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='delivery',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='name',
            field=models.CharField(default='type your name', max_length=200),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='overall',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='quality',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
        ),
    ]
