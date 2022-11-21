# Generated by Django 4.1 on 2022-11-21 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.CharField(choices=[('pycharm', 'Pycharm'), ('vscode', 'VSCode'), ('python', 'Python'), ('java', 'Java'), ('mysql', 'MySql'), ('ecllipse', 'Ecllipse'), ('other', 'Other')], default='other', max_length=100)),
                ('Reason', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BookingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking', models.CharField(choices=[('cubical', 'Cubical'), ('training room', 'Training Room'), ('board room', 'Board Room'), ('interview room', 'Interview Room'), ('other', 'Other')], default='other', max_length=100)),
                ('Reason', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Products', models.CharField(choices=[('bag', 'Bag'), ('laptop', 'Laptop'), ('mouse', 'Mouse'), ('headset', 'Headset'), ('keyboard', 'Keyboard'), ('other', 'Other')], default='other', max_length=100)),
                ('Reason', models.TextField()),
            ],
        ),
    ]