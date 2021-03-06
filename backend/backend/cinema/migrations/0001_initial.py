# Generated by Django 3.1.6 on 2021-02-04 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1500)),
                ('price', models.IntegerField()),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cinema.manager')),
                ('producer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cinema.producer')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cinema.service')),
            ],
        ),
        migrations.CreateModel(
            name='Ordering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
                ('add_comments', models.CharField(max_length=400)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.manager')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.producer')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.service')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('is_edited', models.BooleanField(default=False)),
                ('message_text', models.CharField(max_length=1000)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.manager')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.producer')),
            ],
        ),
    ]
