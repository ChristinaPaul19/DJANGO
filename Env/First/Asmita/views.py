from django.shortcuts import render
from .models import Contact
from .forms import ContactForm

def home(request):
    return render(request, 'home.html')
# Create your views here.
def contacts(request):
    return render(request, 'contacts.html')

def Book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # You can save the data to the database or perform other actions here
        Contact.objects.create(name=name, email=email, message=message)
        return render(request, 'home.html')  # Redirect to a success page after saving
    return render(request, 'book.html')
def viewBooks(request):
    Books = Contact.objects.all()
    return render(request, 'view_books.html', {'Books': Books})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})