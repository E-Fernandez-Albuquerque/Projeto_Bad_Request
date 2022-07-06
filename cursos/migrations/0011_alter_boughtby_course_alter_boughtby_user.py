# Generated by Django 4.0.4 on 2022-06-27 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cursos', '0010_boughtby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boughtby',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buy', to='cursos.course'),
        ),
        migrations.AlterField(
            model_name='boughtby',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buy', to=settings.AUTH_USER_MODEL),
        ),
    ]