# Generated by Django 5.1.2 on 2024-10-22 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('strengths', models.TextField()),
                ('weakness', models.TextField()),
                ('opportunity', models.TextField()),
                ('threat', models.TextField()),
                ('improvements', models.TextField(blank=True, null=True)),
                ('addons', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
