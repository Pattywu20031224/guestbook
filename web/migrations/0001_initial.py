# Generated by Django 2.2.5 on 2020-06-04 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, verbose_name='姓名')),
                ('subject', models.CharField(max_length=200, verbose_name='主題')),
                ('content', models.TextField(verbose_name='內容')),
                ('publication_date', models.DateTimeField(auto_now_add=True, verbose_name='留言時間')),
            ],
        ),
    ]