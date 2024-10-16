from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
    class Meta:
        model = Product
        fields = ('name',
                  'manufactured_at',
                  'image',
                  'price_pay',
                  'description',
                  'category',
                  )  # перечисляем поля для отображения

    def clean_name(self):
        clean_name = self.cleaned_data.get('name')
        for word in self.bad_words:
            if word in clean_name:
                raise ValidationError(f'{word}- такое слово недопустимо')
        return clean_name


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = ('product', 'name_version', 'num_version')  #перечисляем поля для отображения


class ProductModeratorForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Product
        fields = ("description", "category", "is_published")
