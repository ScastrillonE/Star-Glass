from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Nombre',
    )
    email = forms.EmailField(
        label='Correo Electronico',
    )
    subject = forms.CharField(
        label='Asunto',
    )
    message = forms.CharField(
        label='Mensaje',widget=forms.Textarea,
    )


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})

