# Generated by Django 4.1 on 2023-09-28 00:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tienda', '0004_alter_cliente_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalCliente',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellidos', models.CharField(max_length=100)),
                ('dni', models.CharField(db_index=True, max_length=8)),
                ('telefono', models.CharField(db_index=True, max_length=9)),
                ('direccion', models.TextField()),
                ('email', models.EmailField(db_index=True, max_length=254)),
                ('fecha_de_nacimiento', models.DateField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical cliente',
                'verbose_name_plural': 'historical clientes',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
