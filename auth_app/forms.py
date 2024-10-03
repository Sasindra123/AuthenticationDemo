from django import forms

class AccountDeletionForm(forms.Form):
    confirmation = forms.BooleanField(label='I confirm that I want to delete my account', required=True)