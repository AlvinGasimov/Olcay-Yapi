from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Branch

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mesajınız uğurla göndərildi.")
            return redirect('contact:contact')
    else:
        form = ContactForm()
        
    branches = Branch.objects.all()
    
    return render(request, 'contact.html', {'form': form, 'branches' : branches})
