# Generated by Django 4.1.4 on 2022-12-21 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcommerceApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hedar',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='hedarimg'),
        ),
        migrations.AlterField(
            model_name='newarrivals',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='newArrivalsimg'),
        ),
        migrations.AlterField(
            model_name='newarrivalssecond',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='newArrivalsSecondimg'),
        ),
        migrations.AlterField(
            model_name='newproducts',
            name='Img',
            field=models.ImageField(upload_to='', verbose_name='newProductimg'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='newsletterimg'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='Slideimg'),
        ),
        migrations.AlterField(
            model_name='toprated',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='TopRatedimg'),
        ),
        migrations.AlterField(
            model_name='topratedsecond',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='TopRatedSecondimg'),
        ),
        migrations.AlterField(
            model_name='trending',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='trendingimg'),
        ),
        migrations.AlterField(
            model_name='trendingsecond',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='trendingSecondimg'),
        ),
    ]
