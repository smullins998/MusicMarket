from django import forms


class OrderSubmit(forms.Form):
    num_shares = forms.IntegerField(
        label='Shares',
        widget=forms.TextInput(attrs={'style': 'width: 150px; height: 30px;'}),  # Adjust the width as needed
    )    
    buysell_choices = (('buy','buy'), ('sell','sell'))
    buysell = forms.ChoiceField(choices=buysell_choices)
    type_choices = (('market','market'), ('limit','limit'))
    type = forms.ChoiceField(choices=type_choices, widget=forms.RadioSelect)


class Register(forms.Form):
    username = forms.CharField(max_length=70)
    password = forms.CharField(max_length=70)
    confirm_password = forms.CharField(max_length=70)