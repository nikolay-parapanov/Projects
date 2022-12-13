from django import forms
from tri.marketplace import models


class MarketplaceItemCreateForm(forms.ModelForm):

    class Meta:
        model = models.MarketItems
        fields = ('name', 'description', 'price', 'type')
        labels = {
            'name': 'name',
            'description': 'description',
            'price': 'price:',
            'type': 'type',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Item name'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Short description of the item',
                    'cols': 60,
                    'rows':5
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price (in EUR)',
                }
            )
        }
