# Generated by Django 3.2 on 2021-04-19 22:02

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
            name='Enseignant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departement', models.CharField(max_length=50)),
                ('grade', models.CharField(max_length=50)),
                ('salaire', models.FloatField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('titre', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('keyword', models.CharField(max_length=50)),
                ('difficulte', models.CharField(max_length=50)),
                ('domaine', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialite', models.CharField(max_length=50)),
                ('promotion', models.CharField(max_length=50)),
                ('niveau', models.CharField(max_length=50)),
                ('enseignant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users_control.enseignant')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users_control.theme')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChefSep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salaire', models.FloatField()),
                ('role', models.CharField(max_length=25)),
                ('enseignant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users_control.enseignant')),
            ],
        ),
    ]
