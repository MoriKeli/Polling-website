# Generated by Django 4.0.3 on 2022-08-02 08:01

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
            name='UserProfile',
            fields=[
                ('id', models.CharField(editable=False, max_length=16, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('name', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profiles',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.CharField(editable=False, max_length=16, primary_key=True, serialize=False)),
                ('question_text', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('set_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='polls.userprofile')),
            ],
            options={
                'verbose_name_plural': 'Questions',
                'ordering': ['question_text'],
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.CharField(editable=False, max_length=16, primary_key=True, serialize=False)),
                ('option', models.CharField(max_length=300, null=True)),
                ('total_votes', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question')),
            ],
            options={
                'verbose_name_plural': 'Choices',
                'ordering': ['option'],
            },
        ),
    ]
