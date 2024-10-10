from django import forms

input_style = {'style': 'width: 100px; height: 30px; '}

class OrderSubmit(forms.Form):
    num_shares = forms.IntegerField(
        label='Shares',
        widget=forms.TextInput(attrs=input_style),
    )    
    buysell_choices = (('buy','Buy'), ('sell','Sell'))
    buysell = forms.ChoiceField(
        label='Order',
        choices=buysell_choices,
        widget=forms.Select(attrs=input_style)
    )
    type_choices = (('market','Market'), ('limit','Limit'))
    type = forms.ChoiceField(
        label='Limit/Market',
        choices=type_choices,
        widget=forms.Select(attrs=input_style)
    )
    limit_price = forms.IntegerField(
        label='LimitPrice',
        widget=forms.TextInput(attrs=input_style),
    )

class Register(forms.Form):
    username = forms.CharField(max_length=70)
    password = forms.CharField(max_length=70)
    confirm_password = forms.CharField(max_length=70)