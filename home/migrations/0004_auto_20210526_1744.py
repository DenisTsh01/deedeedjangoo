# Generated by Django 3.2.2 on 2021-05-26 14:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210524_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('percentage', models.IntegerField(default=0)),
                ('current_money', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RenameField(
            model_name='taskcategory',
            old_name='task_cateogry',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='userpayment',
            old_name='user_payment_product',
            new_name='budget_name',
        ),
        migrations.RenameField(
            model_name='userpayment',
            old_name='user_payment_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='userpayment',
            old_name='user_payment_type',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='userpocket',
            name='user_budget_emergency',
        ),
        migrations.RemoveField(
            model_name='userpocket',
            name='user_budget_food',
        ),
        migrations.RemoveField(
            model_name='userpocket',
            name='user_budget_investments',
        ),
        migrations.RemoveField(
            model_name='userpocket',
            name='user_budget_wants',
        ),
        migrations.RemoveField(
            model_name='userpocket',
            name='user_expense_education',
        ),
        migrations.RemoveField(
            model_name='userpocket',
            name='user_expense_health_care',
        ),
        migrations.RemoveField(
            model_name='userpocket',
            name='user_expense_housing',
        ),
        migrations.RemoveField(
            model_name='userpocket',
            name='user_expense_other',
        ),
        migrations.RemoveField(
            model_name='userpocket',
            name='user_expense_personal_family',
        ),
        migrations.RemoveField(
            model_name='userpocket',
            name='user_expense_rent',
        ),
        migrations.RemoveField(
            model_name='userpocket',
            name='user_expense_transportation',
        ),
        migrations.RemoveField(
            model_name='userpocket',
            name='user_income',
        ),
        migrations.RemoveField(
            model_name='userpocket',
            name='user_income2',
        ),
        migrations.RemoveField(
            model_name='userpocket',
            name='user_income3',
        ),
        migrations.RemoveField(
            model_name='userpocket',
            name='user_income4',
        ),
        migrations.RemoveField(
            model_name='userpocket',
            name='user_income_date1',
        ),
        migrations.RemoveField(
            model_name='userpocket',
            name='user_income_date2',
        ),
        migrations.RemoveField(
            model_name='userpocket',
            name='user_income_date3',
        ),
        migrations.RemoveField(
            model_name='userpocket',
            name='user_income_date4',
        ),
        migrations.RemoveField(
            model_name='userpocket',
            name='user_income_total',
        ),
        migrations.RemoveField(
            model_name='userpocket',
            name='user_taxes_date',
        ),
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.taskcategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='task_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userpocket',
            name='payment',
            field=models.ManyToManyField(to='home.UserPayment'),
        ),
        migrations.AddField(
            model_name='userpocket',
            name='budgets',
            field=models.ManyToManyField(to='home.Budget'),
        ),
        migrations.AddField(
            model_name='userpocket',
            name='expenses',
            field=models.ManyToManyField(to='home.Expense'),
        ),
        migrations.AddField(
            model_name='userpocket',
            name='incomes',
            field=models.ManyToManyField(to='home.Income'),
        ),
    ]