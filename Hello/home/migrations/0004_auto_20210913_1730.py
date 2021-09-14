# Generated by Django 3.2.7 on 2021-09-13 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210913_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('HIGH', 'HIGH'), ('LOW', 'LOW'), ('MEDIUM', 'MEDIUM')], max_length=10),
        ),
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('COMPLETED', 'COMPLETED'), ('PENDING', 'PENDING')], max_length=10),
        ),
    ]
