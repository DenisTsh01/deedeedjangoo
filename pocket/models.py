from django.db import models
from django.utils import timezone
from users.models import ExtendUser
from django.contrib.auth.models import User

executability = (
    ('Monthly', 'Monthly'),
    ('Weekly', 'Weekly'),
    ('Daily', 'Daily'),
    ('Only once', 'Only once')

)


class IncomeType(models.Model):
    name = models.CharField(max_length=50)
    value = models.DecimalField(decimal_places=2, max_digits=10)
    extend_user = models.ForeignKey(ExtendUser, on_delete=models.CASCADE, null=True)
    execute = models.CharField(max_length=50, default='Monthly', choices=executability, null=False)
    monthly_date = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Income(models.Model):
    income_type = models.ForeignKey(IncomeType, on_delete=models.CASCADE, null=True, blank=True,
                                    related_name='income_id')
    date = models.DateTimeField(default=timezone.now(), null=False)
    extend_user = models.ForeignKey(ExtendUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.income_type


class ExpenseType(models.Model):
    name = models.CharField(max_length=50)
    value = models.DecimalField(decimal_places=2, max_digits=10)
    extend_user = models.ForeignKey(ExtendUser, on_delete=models.CASCADE, null=True)
    monthly_date = models.IntegerField(default=1)

    def __str__(self):
        return self.name



class Expense(models.Model):
    expense_type = models.ForeignKey(ExpenseType, on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='expense_id')
    date = models.DateTimeField(default=timezone.now(), null=False)
    extend_user = models.ForeignKey(ExtendUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.expense_type


class Budget(models.Model):
    name = models.CharField(max_length=50)
    percentage = models.IntegerField(default=0)
    value = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    after_payments = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    extend_user = models.ForeignKey(ExtendUser, on_delete=models.CASCADE, null=True)
    value_accessed = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    def __str__(self):
        return self.name


class Taxes(models.Model):
    name = models.CharField(max_length=50)
    value = models.DecimalField(decimal_places=2, max_digits=10)
    extend_user = models.ForeignKey(ExtendUser, on_delete=models.CASCADE, null=True)
    budget_accessed = models.ForeignKey(Budget, on_delete=models.CASCADE, null=True, blank=True,
                                        db_column='budget_accessed_id')

    def __str__(self):
        return self.name


class UserPocket(models.Model):
    incomes = models.ManyToManyField(Income)
    expenses = models.ManyToManyField(Expense)
    budgets = models.ManyToManyField(Budget)
    income_types = models.ManyToManyField(IncomeType)
    expense_types = models.ManyToManyField(ExpenseType)
    taxes = models.ManyToManyField(Taxes)
