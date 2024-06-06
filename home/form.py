from django import forms
from .models import Portfolio

class PortfolioForm(forms.ModelForm):
    class Meta:
        model=Portfolio
        fields=["ad","soyad","ataadi","yas","tel","email","unvan","tehsil","isyeri","vezife"]
    def __init__(self, *args, **kwargs):
        super(PortfolioForm, self).__init__(*args, **kwargs)
        self.fields['ad'].widget.attrs.update({'class': 'form-control'})
        self.fields['soyad'].widget.attrs.update({'class': 'form-control'})
        self.fields['ataadi'].widget.attrs.update({'class': 'form-control'})
        self.fields['yas'].widget.attrs.update({'class': 'form-control'})
        self.fields['tel'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['unvan'].widget.attrs.update({'class': 'form-control'})
        self.fields['tehsil'].widget.attrs.update({'class': 'form-control'})
        self.fields['isyeri'].widget.attrs.update({'class': 'form-control'})
        self.fields['vezife'].widget.attrs.update({'class': 'form-control'})