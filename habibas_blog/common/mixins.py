from django import forms

class DisabledFieldsFormMixin:
    disabled_fields = '__all__'
    fields = {}

    def _init_disabled_fields(self):
        for name, field in self.fields.items():
            if self.disabled_fields != '__all__' and name not in self.disabled_fields:
                continue

            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            field.widget.attrs['disabled'] = True
            field.required = False
            # if isinstance(field, forms.ChoiceField):
            #     field.widget.attrs['disabled'] = True
            #     field.required = False
            # else:
            #     field.widget.attrs['readonly'] = 'readonly'
