# Generated by Django 4.1.4 on 2022-12-20 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(choices=[('NF', 'Netflix'), ('AP', 'Amazon Video'), ('ST', 'Start+'), ('PM', 'Paramount+')], default='NF', max_length=2)),
                ('fecha_pago', models.DateField(auto_now_add=True)),
                ('monto', models.FloatField(default=0.0)),
            ],
        ),
    ]
