from django import forms
from django.forms import ModelForm
from app.utils import generate_bootstrap_widgets_for_all_fields

from . import (
    models
)


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'phone' or field_name == 'telefone':
                field.widget.attrs['class'] = 'form-control telefone'
            if field_name == 'numero' or field_name == 'number':
                field.widget.attrs['class'] = 'form-control numero'


class DrawForm(BaseForm, ModelForm):
    class Meta:
        model = models.Draw
        fields = '__all__'
        widgets = generate_bootstrap_widgets_for_all_fields(models.Draw)

    def __init__(self, *args, **kwargs):
        super(DrawForm, self).__init__(*args, **kwargs)


class BoxForm(BaseForm, ModelForm):
    class Meta:
        model = models.Box
        fields = ['draw', 'comprimento', 'espessura', ]
        widgets = generate_bootstrap_widgets_for_all_fields(models.Box)

    def __init__(self, *args, **kwargs):
        super(BoxForm, self).__init__(*args, **kwargs)
