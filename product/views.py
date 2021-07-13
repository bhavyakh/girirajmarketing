from django.shortcuts import render

# Create your views here.
def product_view(request, *args, **kwargs):
    # return  HttpResponse("hp")
    return render(request,"product.html", {})
