# Generated by Django 2.2.14 on 2020-07-08 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Coca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_reporte', models.TextField()),
                ('autor', models.TextField()),
                ('encargado', models.TextField()),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha_reporte', models.DateTimeField(blank=True, null=True)),
                ('ID_prueba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
