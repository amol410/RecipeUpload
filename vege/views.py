from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *



# Create your views here.

def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        
# we are saving data into the model 
        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image,)
# below line after submitting data redirecting to the same page i.e homepage
        return redirect('/')

    queryset = Receipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))



    context = {'receipes' : queryset}
    return render(request, 'vege/receipes.html', context)

def update_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        
        
        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/')

    context = {'receipe' : queryset}
    return render(request, 'vege/ureceipe.html', context)


def delete_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/')



        
    
