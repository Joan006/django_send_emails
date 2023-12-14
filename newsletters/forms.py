from django import forms
# importamos los modelos para form
from .models import NewsletterUser, Newsletter

# creacion de formularios 
class NewsletterUserSignUpForm(forms.ModelForm):
    class meta:
        model = NewsletterUser
        fields = ['email']


class NewsletterCreationForm(forms.ModelForm):
    class meta:
        model = Newsletter
        fields = ['user','subject','body','email']

