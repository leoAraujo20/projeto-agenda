from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
from django.core.paginator import Paginator
from contact.forms import ContactForm
from django.urls import reverse

# Create your views here.
def index(request):
    contacts = Contact.objects.filter(show=True).order_by("-id")
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
   
    context = {
        "page_obj": page_obj,
        "page_title": "Contatos"
    }

    return render(request, "contact/index.html", context)

def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    context = {
        "contact": single_contact,
        "page_title": single_contact.first_name
    }

    return render(request, "contact/contact.html", context)

def search(request):
    search_value = request.GET.get("q", '').strip()
    
    if search_value == "":
        return redirect("contact:index")
    
    contacts = Contact.objects.filter(
        Q(first_name__icontains=search_value) |
        Q(last_name__icontains=search_value) |
        Q(phone__icontains=search_value) |
        Q(email__icontains=search_value)
    ).order_by("-id")

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "page_title": "Resultado da busca",
        "search_value": search_value,
    }
    
    return render(request, "contact/index.html", context=context)

def create(request):
    url = reverse("contact:create")
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("contact:index")
    else:
        form = ContactForm()
    
    context = {
        "url": url,
        "form": form,
        "page_title": "Criar contato"
    }
    return render(request, 'contact/create.html', context)

def update(request, contact_id):
    url = reverse("contact:update", kwargs={"contact_id": contact_id})
    contact_obj = get_object_or_404(Contact, pk=contact_id, show=True)
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES, instance=contact_obj)
        if form.is_valid():
            form.save()
            return redirect("contact:index")
    else:
        form = ContactForm(instance=contact_obj)
    
    context = {
        "url": url,
        "form": form,
        "page_title": "Atualizar contato"
    }

    return render(request, "contact/create.html", context)

def delete(request, contact_id):
    contact_obj = get_object_or_404(Contact, pk=contact_id)
    contact_obj.delete()
    return redirect("contact:index")