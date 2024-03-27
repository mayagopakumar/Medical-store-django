from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Medicines
from .forms import MedicinesForm
from django.contrib.auth.decorators import login_required

# add medicines

@login_required(login_url='/login/')
def medicine_create(request):
    if request.method == 'POST':
        form = MedicinesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('readmedicine')
    else:
        form =MedicinesForm()
    return render(request, 'create.html', {'form': form})

# read medicines

@login_required(login_url='/login/')
def medicine_read(request):
    medicine_list=Medicines.objects.all()
    return render(request,'retrieve.html',{'medicine_list':medicine_list})

# edit medicines

@login_required(login_url='/login/')
def medicine_edit(request, id):
    medicine = Medicines.objects.get(pk=id)
    if request.method == 'POST':
        form = MedicinesForm(request.POST,instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('readmedicine')
    else:
        form =MedicinesForm(instance=medicine)           
    return render(request, 'update.html', {'form': form})

# delete medicines

@login_required(login_url='/login/')
def medicine_delete(request,pk):
    medicine=Medicines.objects.get(pk=pk)  
    if request.method == 'POST':
        medicine.delete()
        return redirect('readmedicine')
    
    return render(request,'delete.html',{'medicine':medicine})

# listing medicines

@login_required(login_url='/login/')
def listing(request):
    medicine_list = Medicines.objects.all()
    paginator = Paginator(medicine_list, 10)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'list.html', {'page_obj': page_obj})

# search medicines

@login_required(login_url='/login/')
def medicine_search(request):
    query = request.GET.get('q')
    if query:
        medicine = Medicines.objects.filter(name__icontains=query)
    else:
        medicine = Medicines.objects.all()
    return render(request,'search.html',{'medicine':medicine})



