# Generated by Django 3.0.6 on 2020-05-22 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bomapp', '0002_auto_20200522_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='parts',
        ),
        migrations.CreateModel(
            name='BOM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bomapp.Part')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bomapp.Product')),
            ],
        ),
    ]
