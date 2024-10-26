from django.shortcuts import render
from django.contrib import messages
from .models import Contact

def Contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        number = request.POST.get('number')
        print(name, email, number, content)
        
        if name and 1 < len(name) < 30:
            pass
        else:
            messages.error(request, 'Name length should be between 2 and 30 characters.')
            return render(request, 'home.html')

        if email and 1 < len(email) < 30:
            pass
        else:
            messages.error(request, 'Email length should be between 2 and 30 characters.')
            return render(request, 'home.html')

        if number and 2 < len(number) < 13:
            pass
        else:
            messages.error(request, 'Number length should be between 3 and 12 characters.')
            return render(request, 'home.html')

        # Save the contact data
        ins = Contact(name=name,email=email,content=content,number=number)
        ins.save()
        messages.success(request, 'Thanks for contacting me')
        print('Data has been saved to the database')

    return render(request, 'home.html')

  
  