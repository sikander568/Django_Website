from django.shortcuts import render, HttpResponse
from datetime import datetime
from new.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
      context = {
          'variable':"This is sent"
    }
      messages.success(request,"thhis is test")
      return render(request,'index.html',context)

    # return HttpResponse("This is home page")

def about(request):
    if request.method == "POST":
        # name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc') 
        contact = Contact( email = email, phone = phone, desc = desc, date = datetime.today())
        contact.save()
        messages.success(request,"your message has been successfully")
    return render(request, 'about.html', {'error': 'An error occurred while saving the contact.'})
    
    # return render(request, 'about.html')



def servicer(request):
    return render(request,'servicer.html')
   # return HttpResponse("This is services Page")