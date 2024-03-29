# Generated by Django 2.1.1 on 2019-10-14 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAIBLE', 'Ready to be purchased'), ('SOLD', 'Item sold'), ('RESTOCKING', 'Item restockin in few days')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAIBLE', 'Ready to be purchased'), ('SOLD', 'Item sold'), ('RESTOCKING', 'Item restockin in few days')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAIBLE', 'Ready to be purchased'), ('SOLD', 'Item sold'), ('RESTOCKING', 'Item restockin in few days')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
