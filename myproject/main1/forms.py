from django import forms

input_style = {'style': 'width: 80px; height: 25px; '}

class OrderSubmit(forms.Form):
    num_shares = forms.IntegerField(
        label='Shares',
        widget=forms.TextInput(attrs=input_style), 
  
        # Adjust the width as needed
    )    
    buysell_choices = (('buy','Buy'), ('sell','Sell'))
    buysell =forms.CharField(label='Order', widget=forms.Select(choices=buysell_choices, attrs=input_style))
    type_choices = (('market','Market'), ('limit','Limit'))
    type = forms.CharField(label='Limit/Market', widget=forms.Select(choices=type_choices, attrs=input_style))
    limit_price = forms.IntegerField(
        label='LimitPrice',
        widget=forms.TextInput(attrs=input_style), )
  

class Register(forms.Form):
    username = forms.CharField(max_length=70)
    password = forms.CharField(max_length=70)
    confirm_password = forms.CharField(max_length=70)