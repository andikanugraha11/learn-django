# Generated by Django 2.1.4 on 2019-01-06 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_example_app', '0002_programmer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='programmer',
            name='language',
            field=models.ManyToManyField(to='model_example_app.Language'),
        ),
    ]
