from django import forms
from .models import CustomerOrder


class OrderForm(forms.ModelForm):
    class Meta:
        model = CustomerOrder
        fields = ('full_name', 'email',
                  'address1', 'address2',
                  'postcode', 'county', 'country',
                  'telephone',)

    def __init__(self, *args, **kwargs):
        """ 
        Placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'telephone': 'Phone Number',
            'country': 'Country',
            'postcode': 'Post Code',
            'address1': 'Address Line 1',
            'address2': 'Address Line 2',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
