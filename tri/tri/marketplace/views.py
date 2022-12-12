from django import forms
from django.views import generic as views
from tri.marketplace import models as models
from tri.marketplace.models import MarketItems


class MarketplaceListView(views.ListView):
    model = models.MarketItems
    template_name = 'marketplace/marketplace-list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('id')

        pattern = self.__get_pattern()
        if pattern:
            queryset = queryset.filter(name__icontains=pattern.lower())
        return queryset

    def __get_pattern(self):
        pattern = self.request.GET.get('pattern', None)
        return pattern.lower() if pattern else None


class MarketplaceDetailsView(views.DetailView):
    template_name = 'marketplace/marketplace-detail.html'
    model = models.MarketItems

class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = models.MarketItems
        exclude = ['user_id']
        labels = {
            'name': 'name',
            'description': 'description',
            'price': 'price:',
            'type': 'Date of Birth',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Item name'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Short description of the item'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price (in EUR)',
                }
            ),
            'type': forms.Select(
                attrs={
                    'placeholder': 'Select from the dropdown options',
                }
            )
        }

class MarketplaceItemCreateView(views.CreateView, ItemCreateForm):
    template_name = 'marketplace/marketplace-item-add.html'
    model = models.MarketItems
    # fields = ['name', 'description', 'price', 'type']

    form_class = ItemCreateForm

    # success_url = reverse_lazy('marketplace item details')

    # def get_success_url(self):
    #     created_object = self.object
    #     return reverse_lazy('marketplace details item', kwargs={
    #         pk:created_object.id
    #     })
