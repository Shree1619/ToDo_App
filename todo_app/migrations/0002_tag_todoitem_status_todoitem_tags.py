# Generated by Django 5.0 on 2023-12-28 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='todoitem',
            name='status',
            field=models.CharField(choices=[('OPEN', 'Open'), ('WORKING', 'Working'), ('DONE', 'Done'), ('OVERDUE', 'Overdue')], default='OPEN', max_length=10),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='tags',
            field=models.ManyToManyField(blank=True, to='todo_app.tag'),
        ),
    ]