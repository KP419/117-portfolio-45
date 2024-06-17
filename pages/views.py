from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    form = ContactForm()
    return render(request, 'pages/contact.html', {"form": form})


def contact(request):
    if request.method == "POST":
        form =ContactForm(request.POST)
        
        if form.is_valid():
            # send email
            email_to ="koryplotts@yahoo.com"
            email_from = form.cleaned_data["email"]
            name = form.cleaned_data["name"]
            message = form.cleaned_data["message"]
            
            html = render_to_string("pages/email.html", request.POST)
            
            send_mail(
                "Message from " + name,
                message,
                email_from,
                [email_to],
                html_message=html
            )
            
            return redirect("home")
            
    else:
        form = ContactForm()
        
    return render(request, 'pages/contact.html', {"form": form})