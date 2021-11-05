from django import forms
from .models import Categoria


class CategoriaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['style'] = 'font-size: 14px'
            form.field.widget.attrs['class'] = 'form-control'
        # self.fields['descripcion'].widget.attrs['class'] = 'text-input'
        self.fields['estado'].widget.attrs['type'] = 'checkbox'
        self.fields['descripcion'].widget.attrs['placeholder'] = 'Categoría'

    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        labels = {
            'descripcion': 'Descripcion de la Categoría',
            'estado': 'Estado'
        }
