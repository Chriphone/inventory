# Generated by Django 4.1 on 2022-09-04 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('availlable', 'Item ready to be purchased'), ('SOLD', 'Item sold'), ('RESTOCKING', 'item restoking in few days')], default='SOLD', max_length=10)),
                ('Issues', models.CharField(default='No Issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('availlable', 'Item ready to be purchased'), ('SOLD', 'Item sold'), ('RESTOCKING', 'item restoking in few days')], default='SOLD', max_length=10)),
                ('Issues', models.CharField(default='No Issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('availlable', 'Item ready to be purchased'), ('SOLD', 'Item sold'), ('RESTOCKING', 'item restoking in few days')], default='SOLD', max_length=10)),
                ('Issues', models.CharField(default='No Issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
