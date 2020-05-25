# Generated by Django 3.0.6 on 2020-05-25 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=256)),
                ('emial', models.EmailField(max_length=256, unique=True)),
                ('contact', models.IntegerField(max_length=15)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('n', 'Non Binary'), ('na', 'Prefer not to say')], max_length=2)),
                ('bio', models.TextField()),
                ('tshirt_size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=3, verbose_name='T-Shirt Size')),
                ('skills', models.TextField()),
                ('educational_institution', models.CharField(max_length=128)),
                ('field_of_study', models.CharField(blank=True, choices=[('cs', 'Computer Science'), ('ec', 'Electronics and Communication'), ('me', 'Mechanical Engineering'), ('ce', 'Civil Engineering'), ('ee', 'Electrical and Electronis Engineering'), ('it', 'Information Technology')], max_length=64, verbose_name='Field of Study')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_confirmed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]