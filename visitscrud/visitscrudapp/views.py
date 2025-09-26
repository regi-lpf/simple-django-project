from django.shortcuts import render, redirect
from .models import Visit
from .forms import VisitForm

# Create your views here.
def home(request):
    obj = Visit.objects.all()
    
    return render(request, "home.html", {'obj' : obj})

def create(request):
    form = VisitForm()
    
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form': form}
    
    return render(request, "visit_form.html", context)

def update(request, f_id):
    obj = Visit.objects.get(id=f_id)
    form = VisitForm(instance=obj)
    if request.method == 'POST':
        form = VisitForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'visit_form.html', context)

def delete(request, f_id):
    obj = Visit.objects.get(id=f_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('home')
    context = {'obj': obj}
    return render(request, 'confirmation.html', context)