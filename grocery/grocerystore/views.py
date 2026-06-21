from django.shortcuts import render
from .models import Product
# Create your views here.
def home (req):

    products={}
    if req.GET.get('search'):
        products=Product.objects.filter(name__icontains=req.GET.get('search'))
    else:
        products=Product.objects.all()

    return render(req, 'home.html', {'products':products})