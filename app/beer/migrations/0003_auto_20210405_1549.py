# Generated by Django 3.1.7 on 2021-04-05 15:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0002_beer_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beer',
            old_name='beer_id',
            new_name='api_id',
        ),
        migrations.RemoveField(
            model_name='beer',
            name='hops',
        ),
        migrations.RemoveField(
            model_name='beer',
            name='malt',
        ),
        migrations.CreateModel(
            name='Malt',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('beer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='beer.beer')),
            ],
        ),
        migrations.CreateModel(
            name='Hops',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('beer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='beer.beer')),
            ],
        ),
    ]
