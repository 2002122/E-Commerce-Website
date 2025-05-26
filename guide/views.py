from django.shortcuts import render,redirect, get_object_or_404
from.models import tb_login ,blah
from django.contrib import messages
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')
def login(request):
    if request.method=="POST" :
        try:
            login=tb_login.objects.get(user=request.POST['user'],password=request.POST['pass'])
            return redirect('dashboard')
        except tb_login.DoesNotExist as e:
            return render(request,'home.html')
        
def dashboard(request):
    return render(request,'dashboard.html')

def profile(request):
    return render(request,'profile.html')

def additional(request):
    return render(request,'additional.html')

def add(request):
    if request.method=='POST' and request.FILES.get('image'):
        add=blah(
        product_name=request.POST.get('product_name'),
        category=request.POST.get('category'),
        image_url=request.FILES['image'],
        price=request.POST.get('price'),
        quantity=request.POST.get('quantity'),
        description=request.POST.get('description')
        )
        add.save()
        messages.success(request,'Details added successfully...')
        return render(request,'dashboard.html')
    else:
        return render(request,'add.html')
             
def view(request):
    details=blah.objects.all()
    return render(request,'view.html',{'details':details})

def edit_profile(request):
    return render(request,'edit_profile.html')

def edit(request,id):
    editpr = blah.objects.get(id=id)
    return render(request,'edit.html',{'editpr':editpr})

def update(request,id):
    editpr=blah.objects.get(id=id)
    if request.method=='POST':
        editpr.product_name=request.POST.get('product_name')
        editpr.category=request.POST.get('category')
    
        editpr.price=request.POST.get('price')
        editpr.quantity=request.POST.get('quantity')
        editpr.description=request.POST.get('description')
        
        
        if 'image'in request.FILES:
            
            uploaded_image = request.FILES['image']
            file_path = default_storage.save(f'static/images/{uploaded_image.name}', ContentFile(uploaded_image.read()))
            editpr.image_url = file_path

        editpr.save()
        messages.success(request, 'Product updated successfully!')
        return redirect('view')  # Redirect to the correct Django view name

    return render(request, 'edit.html', {'editpr': editpr})
    
    
def destroy(request, id):
    try:
        Del = blah.objects.get(id=id)
        Del.delete()
        return redirect('view')
    except blah.DoesNotExist:
        return HttpResponse("The record you're trying to delete doesn't exist.", status=404)