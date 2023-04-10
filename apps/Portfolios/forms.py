from django import forms
from .models import Portfolio


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ('profile', 'title', 'about_me', 'portfolio_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'about_me': forms.Textarea(attrs={'class': 'form-control'}),
            'profile': forms.Select(attrs={'class': 'form-control'}),
        }
