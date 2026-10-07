from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from smtplib import SMTPException
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm, ContactForm

def about_me_view(request):
    return render(request, 'pages/about_me.html')


def experience_view(request):
    return render(request, 'pages/experience.html')


def send_email(form):
    name = form.cleaned_data["name"]
    email = form.cleaned_data["email"]
    subject = form.cleaned_data["subject"]
    message = form.cleaned_data["message"]

    body = (
        f"Message from your portfolio contact form:\n\n"
        f"Name: {name}\n"
        f"Email: {email}\n\n"
        f"Message:\n{message}"
    )

    return send_mail(
        subject=subject,
        message=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.CONTACT_EMAIL],
        fail_silently=False,
    )


def contact_view(request):
    form = ContactForm(
        request.POST if request.method == "POST" else None
    )

    if request.method == "POST" and form.is_valid():
        try:
            delivered = send_email(form)
        except (BadHeaderError, SMTPException, OSError):
            form.add_error(
                None,
                "Your message could not be sent. Please try again."
            )
        else:
            if delivered == 1:
                return redirect("/contact/?sent=1")

            form.add_error(
                None,
                "Your message could not be sent. Please try again."
            )

    return render(request, "pages/contact.html", {
        "form": form,
        "sent": request.GET.get("sent") == "1",
    })


def projects_view(request):
    projects = Project.objects.all()
    return render(request, 'pages/projects.html', {'projects': projects})

def add_project_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm()

    return render(request, 'pages/add_project.html', {'form': form})