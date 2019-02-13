# Generated by Django 2.1.5 on 2019-02-12 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('educations', '0010_auto_20190208_0357'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Формат курсов',
                'verbose_name_plural': 'Форматы курсов',
            },
        ),
        migrations.AlterField(
            model_name='education',
            name='category',
            field=models.ForeignKey(blank=True, default=None, max_length=64, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='educations.EducationFormat'),
        ),
    ]