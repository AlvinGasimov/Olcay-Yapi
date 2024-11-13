from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['username', 'email', 'phone', 'architect_status', 'message']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Ad', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'required': True}),
            'phone': forms.TextInput(attrs={
                'placeholder': '(_ _) _ _ _-_ _-_ _', 
                'maxlength': '14', 
                'style': 'padding-left: 3.5rem; font-size: 14px'
            }),
            'architect_status': forms.Select(choices=Contact.ARCHITECT_STATUS_CHOICES, attrs={'required': True}),
            'message': forms.Textarea(attrs={'placeholder': 'Bizə mesajınız'}),
        }