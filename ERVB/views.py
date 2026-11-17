from django.shortcuts import render

def home(request):
    return render(request, 'ERVB/home.html')

def menu(request):
    return render(request, 'ERVB/menu.html')

def administration(request):
    return render(request, 'ERVB/administration.html')   

def contact(request):
    return render(request, 'ERVB/contact.html') 