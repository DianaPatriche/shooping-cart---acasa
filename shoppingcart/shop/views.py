from django.shortcuts import render
from .models import Product,Category


# Create your views here.
def product_list(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'list.html',context)


def product_detail(request):
    id=request.GET.get('id')
    p=Product.objects.get(pk=int(id))
    context={'produs':p}
    return render(request,'produs.html',context)

