from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, ContactMessage
from .forms import ContactForm

# Create your views here.

def project_list(request):
    projects = Project.objects.all()
    return render(request, "index.html", {"projects": projects})

def home(request):
    projects = Project.objects.all()
    return render(request, "home.html",{"projects": projects})

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'project_detail.html', {'project': project})


def contact(request):
    if request.method == "POST":  # Si el usuario envía el formulario
        form = ContactForm(request.POST)  
        if form.is_valid():  # Verifica si los datos son correctos
            name = form.cleaned_data['name']  
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Guarda el mensaje en la base de datos
            ContactMessage.objects.create(name=name, email=email, message=message)
            request.session['message_sent'] = True  

            return redirect('contact_success')  # Redirige a una página de éxito
    else:
        form = ContactForm()  # Si es un GET, carga el formulario vacío

    return render(request, "contact.html", {"form": form})  # Renderiza la plantilla

def contact_success(request):
    if not request.session.get('message_sent'):
        return redirect('/')  # Evita acceso manual
    
    del request.session['message_sent']
    
    return render(request, "contact_success.html")