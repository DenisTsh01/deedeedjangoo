# Generated by Django 3.2.2 on 2021-05-24 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_extenduser_city'),
        ('home', '0002_userpayment_userpocket_userstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='extend_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.extenduser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userpocket',
            name='user_income_total',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]
