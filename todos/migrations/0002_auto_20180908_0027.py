# Generated by Django 2.1.1 on 2018-09-07 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='status',
            field=models.CharField(choices=[(1, 'todo'), (2, 'progress'), (3, 'onhold'), (4, 'done')], default=1, max_length=1),
        ),
    ]
