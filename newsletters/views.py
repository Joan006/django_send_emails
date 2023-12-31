from django.core.checks import messages
from django.conf import settings
from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage

from newsletters.models import NewsletterUser
from .forms import NewsletterUserSignUpForm

def newsletter_signup(request):
    form = NewsletterUserSignUpForm (request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, 'Email already exists')

        else:
            instance.save()
            messages.success(request, 'hemos enviado un correo electronico a su correo')
            # correo electronico
            subject ="libro de cocina"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]

            html_template = "newsletters/email_templates/welcome.html" 
            html_message = render_to_string(html_template)
            message = EmailMessage(subject, html_message, from_email, to_email)
            message.content_subtype="html"
            message.send()

    context = {
        "form":form,
    }
    return render(request, 'start-here.html', context)





