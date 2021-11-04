from django.shortcuts import render
from django.http import HttpResponse
from . import models
from hello.models import Contact
# Create your views here.
def index(request):
    return HttpResponse("Heloo i am hello apps index page!")

def table(request):
    return render(request, 'index.html')
def popup(request):
    if request.method == "POST":
        # Fetching the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        # comment = request.POST["comment"]
        # status = request.POST["status"]

        # Saving the information in the database
        # document = models.Document(
        #     comment = comment,
        #     status = status
        # )
        # document.save()
        contact = models.Contact(
            name=name,
            email=email,
            phone=phone
        )
        contact.save()

    documents = models.Document.objects.all() 
    return render(request,'popup.html',context = {
        "files": documents})
def dyform(request):
    return render(request,'dyform.html')