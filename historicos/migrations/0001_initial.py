# Generated by Django 3.2.7 on 2021-11-04 23:51

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricoModel',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(db_column='ID', default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('data_entrada', models.DateField(auto_now=True)),
                ('funcionario', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=7)),
                ('descricao', models.TextField()),
                ('quantidade', models.PositiveSmallIntegerField()),
                ('produto_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='produtos.produtomodel')),
            ],
            options={
                'verbose_name': 'Historico',
                'verbose_name_plural': 'Historicos',
                'db_table': 'HISTORICO',
            },
        ),
    ]
