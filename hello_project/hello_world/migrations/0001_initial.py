# Generated by Django 3.1.6 on 2021-02-04 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table1',
            fields=[
                ('table_1_id', models.AutoField(primary_key=True, serialize=False)),
                ('field_1', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Table2',
            fields=[
                ('table_2_id', models.AutoField(primary_key=True, serialize=False)),
                ('field_2', models.TextField(blank=True, null=True)),
                ('table_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_items', to='hello_world.table1')),
            ],
        ),
    ]