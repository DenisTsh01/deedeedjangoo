from django.urls import path

from pocket.views import IncomeCreateView, BudgetCreateView, ExpenseCreateView, \
    WalletTemplateView, WalletListView, IncomeListView, ExpenseListView, BudgetListView, \
    IncomeUpdateView, ExpenseUpdateView, BudgetUpdateView, IncomeDeleteView, ExpenseDeleteView, \
    BudgetDeleteView, ExpenseTypeCreateView, IncomeTypeCreateView, TaxesCreateView

urlpatterns = [

    path('income_add/', IncomeCreateView.as_view(), name='income_add'),
    path('budget_add/', BudgetCreateView.as_view(), name='budget_add'),
    path('expense_add/', ExpenseCreateView.as_view(), name='expense_add'),
    path('expense_type_add/', ExpenseTypeCreateView.as_view(), name='expense_type_add'),
    path('taxes_add/', TaxesCreateView.as_view(), name='taxes_add'),
    path('income_type_add/', IncomeTypeCreateView.as_view(), name='income_type_add'),
    # path('payment_add/', PaymentCreateView.as_view(), name='payment_add'),
    path('wallet_main/', WalletTemplateView.as_view(), name='wallet_main_page'),
    path('wallet_view/', WalletListView.as_view(), name='wallet_list_view'),
    path('income_view/',   IncomeListView.as_view(), name='income_list_view'),
    path('expense_view/', ExpenseListView.as_view(), name='expense_list_view'),
    path('budget_view/', BudgetListView.as_view(), name='budget_list_view'),
    # path('payment_view/', PaymentListView.as_view(), name='payment_list_view'),
    path('income_update/<int:pk>/', IncomeUpdateView.as_view(), name='income_update'),
    path('expense_update/<int:pk>/', ExpenseUpdateView.as_view(), name='expense_update'),
    path('budget_update/<int:pk>/', BudgetUpdateView.as_view(), name='budget_update'),
    # path('payment_update/<int:pk>/', PaymentUpdateView.as_view(), name='payment_update'),
    path('income_delete/<int:pk>/', IncomeDeleteView.as_view(), name='income_delete'),
    path('expense_delete/<int:pk>/', ExpenseDeleteView.as_view(), name='expense_delete'),
    path('budget_delete/<int:pk>/', BudgetDeleteView.as_view(), name='budget_delete'),
    # path('payment_delete/<int:pk>/', PaymentDeleteView.as_view(), name='payment_delete'),

]

