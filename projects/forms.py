from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=100)
    email = forms.EmailField(label="Correo Electrónico")
    message = forms.CharField(label="Mensaje", widget=forms.Textarea)
