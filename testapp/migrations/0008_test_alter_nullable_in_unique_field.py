# Generated by Django 3.0.4 on 2020-04-20 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0007_test_remove_onetoone_field_part2'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestAlterNullableInUniqueField',
            fields=[
                ('a', models.CharField(max_length=50, null=True, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='testalternullableinuniquefield',
            name='a',
            field=models.CharField(max_length=50, unique=True),
        )
    ]
