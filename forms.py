from django import forms
from .models import Transaction
from django.contrib.auth.forms import AuthenticationForm
class CustomLoginForm(AuthenticationForm):
    pass
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['Roll', 'Amount', 'Date', 'Transaction_Type']
    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        
        # Set placeholders for each field
        self.fields['Roll'].widget.attrs['placeholder'] = 'Enter Roll'
        self.fields['Amount'].widget.attrs['placeholder'] = 'Enter Amount'
        self.fields['Date'].widget.attrs['placeholder'] = 'Enter Date'
        self.fields['Transaction_Type'].widget.attrs['placeholder'] = 'Select Transaction Type'
