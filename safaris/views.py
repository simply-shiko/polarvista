from django.shortcuts import render, get_object_or_404 
from .models import Destination, Place, SafariPackage

# Homepage: featured safaris
def home(request):
    featured_safaris = SafariPackage.objects.filter(is_featured=True)
    return render(request, 'safaris/home.html', {'featured_safaris': featured_safaris})
def packages(request):
    safaris= SafariPackage.objects.all()
    return render(request, 'safaris/packages.html',{'safaris':safaris})

# All destinations
def destinations(request):
    destinations = Destination.objects.all()
    return render(request, 'safaris/destinations.html', {'destinations': destinations})

# All safari packages
def safari_packages(request):
    packages = SafariPackage.objects.all()
    return render(request, 'safaris/safari_packages.html', {'packages': packages})

# Place detail page
def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    return render(request, 'safaris/place_detail.html', {'place': place})

def safari_detail(request,id):
    safari=get_object_or_404(SafariPackage,id=id)
    return render(request, 'safaris/ safari_detail.html',{'safari':safari})

def places(request):
    places=Place.objects.all()
    return render(request, 'safaris/places.html',{'places':places}) 

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            subject=f'New Contact Message from {name}',
            message=f'Email: {email}\n\nMessage:\n{message}',
            from_email=email,
            recipient_list=['info@polarvista.com'],
        )

        return render(request, 'safaris/contact.html', {'success': True})

    return render(request, 'safaris/contact.html')