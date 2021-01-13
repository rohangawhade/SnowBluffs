from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    context = {
        'variable1': 'This is variable1',
        'variable2': 'This is variable2'
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is homepage")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page")


def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is services page")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')
        contact = Contact(name=name,
                          email=email,
                          phone=phone,
                          comment=comment,
                          date=datetime.today())
        contact.save()
        messages.success(request, 'Thank you for contacting us.')
    return render(request, 'contact.html')
    # return HttpResponse("This is contact page")
