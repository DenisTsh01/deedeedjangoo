from django.forms import TextInput, Select, HiddenInput
from pocket.models import Income, Budget, Expense, ExpenseType, IncomeType, Taxes
from django import forms


class BudgetCreateForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ('name', 'percentage', 'extend_user')
        widgets = {

            'name': TextInput(attrs={
                'placeholder': 'Insert budget name. ',
                'class': 'form-control'
            }),
            'percentage': TextInput(attrs={
                'placeholder': 'Percentage of your left income. ',
                'class': 'form-control'
            }),
            'extend_user': Select(attrs={
                'placeholder': 'Insert value. ',
                'class': 'form-control'
            }),
        }


class ExpenseCreateForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = "__all__"
        # widgets = {
        #
        #     'expense_type': Select(attrs={
        #         'placeholder': 'Insert expense name. ',
        #         'class': 'form-control'
        #     }),
        #     'date': TextInput(attrs={
        #         'placeholder': '(year-month-day) ',
        #         'class': 'form-control'
        #     }),
        #
        # }


class ExpenseTypeCreateForm(forms.ModelForm):
    class Meta:
        model = ExpenseType
        fields = "__all__"
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Insert income name. ',
                'class': 'form-control'
            }),
            'value': TextInput(attrs={
                'placeholder': 'Insert value. ',
                'class': 'form-control'
            }),
            'monthly_date': TextInput(attrs={
                'placeholder': '(year-month-day) ',
                'class': 'form-control'
            }),

            'extend_user': Select(attrs={
                'placeholder': '(year-month-day) ',
                'class': 'form-control',

            }),

        }


class TaxesCreateForm(forms.ModelForm):
    class Meta:
        model = Taxes
        fields = "__all__"
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Insert income name. ',
                'class': 'form-control'
            }),
            'value': TextInput(attrs={
                'placeholder': 'Insert value. ',
                'class': 'form-control'
            }),

            'budget_accessed': Select(attrs={
                'placeholder': ' ',
                'class': 'form-control',

            }),

        }


class IncomeTypeCreateForm(forms.ModelForm):
    class Meta:
        model = IncomeType
        fields = "__all__"
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Insert income name. ',
                'class': 'form-control'
            }),
            'value': TextInput(attrs={
                'placeholder': 'Insert value. ',
                'class': 'form-control'
            }),
            'monthly_date': TextInput(attrs={
                'placeholder': '(year-month-day) ',
                'class': 'form-control'
            }),
            'extend_user': Select(attrs={
                'placeholder': '(year-month-day) ',
                'class': 'form-control',

            }),

        }

    # def __init__(self, *args, **kwargs):
    #     super(IncomeTypeCreateForm, self).__init__(*args, **kwargs)
    #     self.fields['extend_user'].widget = HiddenInput()


class IncomeCreateForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = "__all__"
        # widgets = {
        #     'income_type': Select(attrs={
        #         'placeholder': 'Insert income name. ',
        #         'class': 'form-control'
        #     }),
        #     'date': TextInput(attrs={
        #         'placeholder': '(year-month-day) ',
        #         'class': 'form-control'
        #     }),
        #
        # }
        #
