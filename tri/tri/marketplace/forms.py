from django import forms
from tri.marketplace import models


class MarketplaceItemCreateForm(forms.ModelForm):
    class Meta:
        model = models.MarketItems
        fields = ('name', 'description', 'price', 'type', 'user')
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
                    'rows': 5
                }
            ),
            # 'price': forms.DecimalField(
            #     attrs={
            #         'max_value' : 9999999999.99,
            #         'min_value' : 0.00,
        # }
        # )
        }
