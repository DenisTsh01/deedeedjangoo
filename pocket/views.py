from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, ListView, TemplateView, DeleteView
from pocket.form import IncomeCreateForm, BudgetCreateForm, ExpenseCreateForm, ExpenseTypeCreateForm, \
    IncomeTypeCreateForm, TaxesCreateForm
from pocket.models import UserPocket, Income, Budget, Expense, ExpenseType, IncomeType, Taxes
from users.models import ExtendUser
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt

import sqlite3


# conn = sqlite3.connect('db.sqlite3')
#
# cursor = conn.cursor()
#
# query = """INSERT INTO 'pocket_income'(id,extend_user_id,income_type_id,date)
# values(dsadas,dasdasd,dasdsad,dsadasd);"""

@xframe_options_exempt
def ok_to_load_in_a_frame(request):
    return HttpResponse("This page is safe to load in a frame on any site.")


class ExpenseCreateView(LoginRequiredMixin, CreateView):
    template_name = 'pocket/add_view/expense_add.html'
    model = Expense
    form_class = ExpenseCreateForm
    context_object_name = 'all_expenses'
    success_url = reverse_lazy('wallet_main_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        form = context.get('form', ExpenseCreateForm())
        print(form)
        extend_user = ExtendUser.objects.get(username=self.request.user.username)
        context['extend_user'] = extend_user
        expense_types = ExpenseType.objects.filter(extend_user_id=extend_user.id)
        context['expense_types'] = expense_types

        return context


class IncomeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'pocket/add_view/income_add.html'
    model = Income
    form_class = IncomeCreateForm
    context_object_name = 'all_incomes'
    success_url = reverse_lazy('wallet_main_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        form = context.get('form', IncomeCreateForm())
        print(form)
        extend_user = ExtendUser.objects.get(username=self.request.user.username)
        context['extend_user'] = extend_user
        income_types = IncomeType.objects.filter(extend_user_id=extend_user.id)
        context['income_types'] = income_types

        return context


class TaxesCreateView(LoginRequiredMixin, CreateView):
    template_name = 'pocket/add_view/tax_add.html'
    model = Taxes
    form_class = TaxesCreateForm
    context_object_name = "all_taxes"
    success_url = reverse_lazy('wallet_main_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = context.get('form', TaxesCreateForm())
        print(form)
        extend_user = ExtendUser.objects.get(username=self.request.user.username)
        context['extend_user'] = extend_user
        bugget_data = Budget.objects.filter(extend_user_id=extend_user.id)
        context['budget_type'] = bugget_data

        return context


class ExpenseTypeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'pocket/add_view/expense_type_add.html'
    model = ExpenseType
    form_class = ExpenseTypeCreateForm
    context_object_name = "all_expense_type"
    success_url = reverse_lazy('wallet_main_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        extend_user = ExtendUser.objects.get(username=self.request.user.username)
        context['extend_user'] = extend_user
        print(context)

        return context


class WalletTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'pocket/pocket_main_page.html'


class WalletListView(LoginRequiredMixin, ListView):
    template_name = 'pocket/pocket_list_view.html'
    model = UserPocket
    context_object_name = "all_from_pocket"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        incomes = Income.objects.filter(extend_user_id=self.request.user.id)
        expenses = Expense.objects.filter(extend_user_id=self.request.user.id)
        budgets_data = Budget.objects.filter(extend_user_id=self.request.user.id)
        payments_data = Taxes.objects.filter(extend_user_id=self.request.user.id)
        total_income = 0
        total_expense = 0
        total_payments_value = 0
        saved = 0

        for income in incomes:
            income_type: IncomeType = income.income_type
            total_income += income_type.value

        for expense in expenses:
            expense_type: ExpenseType = expense.expense_type
            total_expense += expense_type.value

        for tax in payments_data:
            total_payments_value += tax.value

        saved = total_income - total_expense
        remained = saved - total_payments_value
        context['remained'] = remained
        context['income'] = total_income
        context['expense'] = total_expense
        context['payments'] = total_payments_value
        context['saved'] = saved
        percent = 100

        for bud in budgets_data:
            bud.value = saved * bud.percentage / 100
            budgets_data.value = bud.value
            bud.after_payments = bud.value

            Budget.objects.filter(pk=bud.id).update(value=bud.after_payments)

        for bud in budgets_data:
            percent = percent - bud.percentage
            saved = saved - bud.value

        difference = abs(percent)

        if percent < 0 :
            context['budget_error_meessage'] = f"Sorry but you passed the limit of 100% of your budgets with {difference} procents"
        else:
            context['budget_error_meessage'] = ""

        context['other_percentage'] = percent
        context['other_value'] = saved

        val_accessed = 0
        for bud in budgets_data:
            for tax in payments_data:
                if bud.id == tax.budget_accessed_id:
                    bud.after_payments -= tax.value
            Budget.objects.filter(pk=bud.id).update(after_payments=bud.after_payments)

            Budget.objects.filter(pk=bud.id).update(value_accessed=bud.value-bud.after_payments)
        context['budgets'] = budgets_data

        return context


class BudgetCreateView(LoginRequiredMixin, CreateView):
    template_name = 'pocket/add_view/budget_add.html'
    model = Budget
    form_class = BudgetCreateForm
    context_object_name = "all_budgets"
    success_url = reverse_lazy('wallet_main_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        extend_user = ExtendUser.objects.get(username=self.request.user.username)
        context['extend_user'] = extend_user
        print(context)

        return context


class IncomeTypeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'pocket/add_view/income_type_add.html'
    model = IncomeType
    form_class = IncomeTypeCreateForm
    context_object_name = 'all_income_type'
    success_url = reverse_lazy('wallet_main_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        extend_user = ExtendUser.objects.get(username=self.request.user.username)
        context['extend_user'] = extend_user
        print(context)

        return context


####################################################
# list view


class BudgetListView(LoginRequiredMixin, ListView):
    template_name = 'pocket/list_view/budget_list_view.html'
    model = Budget
    context_object_name = "all_budgets"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        budget_data = Budget.objects.filter(extend_user_id=self.request.user.id)
        context['budgets'] = budget_data

        return context


class IncomeListView(LoginRequiredMixin, ListView):
    template_name = 'pocket/list_view/income_list_view.html'
    model = Income
    context_object_name = "all_incomes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        income_data_type = IncomeType.objects.filter(extend_user_id=self.request.user.id)
        income_data = Income.objects.filter(extend_user_id=self.request.user.id)

        context['income_data'] = income_data
        return context


class ExpenseListView(LoginRequiredMixin, ListView):
    template_name = 'pocket/list_view/expense_list_view.html'
    model = Expense
    context_object_name = "all_expenses"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        expense_data_type = ExpenseType.objects.filter(extend_user_id=self.request.user.id)
        expense_data = Expense.objects.filter(extend_user_id=self.request.user.id)

        context['expense_data'] = expense_data
        return context


###############################################
# update view

class IncomeUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "pocket/update_view/income_update.html"
    model = Income
    fields = "__all__"
    success_url = reverse_lazy("income_list_view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        form = context.get('form', IncomeCreateForm())
        print(form)
        extend_user = ExtendUser.objects.get(username=self.request.user.username)
        context['extend_user'] = extend_user
        expense_types = ExpenseType.objects.filter(extend_user_id=extend_user.id)
        context['expense_types'] = expense_types

        return context


class BudgetUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "pocket/update_view/budget_update.html"
    model = Budget
    fields = "__all__"
    success_url = reverse_lazy("budget_list_view")


class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "pocket/update_view/expense_update.html"
    model = Expense
    fields = "__all__"
    success_url = reverse_lazy("expense_list_view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        form = context.get('form', ExpenseCreateForm())
        print(form)
        extend_user = ExtendUser.objects.get(username=self.request.user.username)
        context['extend_user'] = extend_user
        expense_types = ExpenseType.objects.filter(extend_user_id=extend_user.id)
        context['expense_types'] = expense_types

        return context


##########################################################
# delete view


class IncomeDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "pocket/delete_view/income_delete.html"
    model = Income
    success_url = reverse_lazy("wallet_main_page")


class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "pocket/delete_view/expense_delete.html"
    model = Expense
    success_url = reverse_lazy("wallet_main_page")


class BudgetDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "pocket/delete_view/budget_delete.html"
    model = Budget
    success_url = reverse_lazy("wallet_main_page")
