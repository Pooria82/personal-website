from django.shortcuts import render
from projects_app.models import Project
from contactus_app.models import Message, Footer


def home(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        if firstname and lastname and email and phone and message:
            Message.objects.create(firstname=firstname, lastname=lastname, email=email, phone=phone, message=message)

    projects = Project.objects.all()
    footer = Footer.objects.all().last()

    return render(request, 'index.html', context={'projects': projects, 'footer': footer})
