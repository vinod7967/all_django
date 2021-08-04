# Generated by Django 3.2.6 on 2021-08-04 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_inher_app', '0002_ano_table_mul_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='proyx_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='stu',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('model_inher_app.proyx_info',),
        ),
    ]