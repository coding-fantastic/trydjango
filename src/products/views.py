from django.shortcuts import render
from .forms import ProductForm , RawProductForm
from .models import Product

# Create your views here.

def product_create_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            # two stars will turn into argument that we are going to pass in the form
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        "form": my_form
    }
    return render(request, "product/product_create.html", context)


# def product_create_view(request):
#     print(request.GET)
#     print(request.POST)
#     if request.method =="POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#
#     context = {
#
#      }
#     return render(request, "product/product_create.html", context)


# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
        # ensure after submit of form return user to a fresh new form
    #     form = ProductForm()
    #
    # context = {
    #     'form': form
    # }
    # return render(request, "product/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)

    context = {
        'object': obj
    }
    return render(request, "product/detail.html", context)
