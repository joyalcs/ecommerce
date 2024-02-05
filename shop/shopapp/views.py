from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .models import Category, Product
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger

# Create your views here.

# class HomeView(View):
#     def get(self, request):
#         return render(request, 'shopapp/home.html')

# class AllCategories(View):
#     def get(self, request,c_slug=None):
#         c_page = None
#         products = None
#         if c_slug!=None:
#             c_page = get_object_or_404(Category, slug=c_slug)
#             products = Product.objects.all().filter(category=c_page, available=True)
#         else:
#             products= Product.objects.all().filter(available=True)

#         context = {
#             'category': c_page,
#             'products': products
#         }
#         return render(request, 'shopapp/home.html', context=context)


def AllCategories(request, c_slug=None):
        c_page = None
        products = None
        if c_slug is not None:
            c_page = get_object_or_404(Category, slug=c_slug)
            products = Product.objects.filter(category=c_page, available=True)
        else:
            products = Product.objects.filter(available=True)
        paginator = Paginator(products, 9)
        page = request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context = {
            'category': c_page,
            'products': products,
            'page': page,
        }
        return render(request, 'shopapp/home.html', context=context)

def ProductDetail(request,c_slug,product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e

    context = {
        'product': product,
    }
    return render(request, 'shopapp/product.html', context=context)


# def Add_to_cart(request):
#     cart_product = {}
#     cart_product[str(request.GET['id'])]={
#         'name': request.GET['name'],
#         'qty': request.GET['qty'],
#         'price': request.GET['price'],
#         'image': request.GET['image']
#     }
#     # pro_qty = Product.objects.get(id=id)
#     # pro_qty.stock-= request.GET['qty']
#     # pro_qty.save()
#     if 'cart_data_obj' in request.session:
#         if str(request.GET['id']) in request.session['cart_data_obj']:
#             cart_data = request.session['cart_data_obj']
#             cart_data[str(request.GET['id'])]['qty'] = int(cart_product[str(request.GET['id'])]['qty'])
#             cart_data.update(cart_data)
#             request.session['cart_data_obj'] = cart_data
#         else:
#             cart_data = request.session['cart_data_obj']
#             cart_data.update(cart_product)
#             request.session['cart_data_obj'] = cart_data
#     else:
#         request.session['cart_data_obj'] = cart_product
#     return JsonResponse({"data":request.session['cart_data_obj'], "totalcartitems":len(request.session['cart_data_obj'])})


# def cart_items(request):
#     cart_total_price = 0
#     if 'cart_data_obj' in request.session:
#         for product_id, item in request.session['cart_data_obj'].items():
#             if 'price' in item and item['price']:
#                 try:
#                     cart_total_price += int(item['qty']) * float(item['price'])
#                 except ValueError:
#                     pass
#         return render(request, 'shopapp/cart.html', {"data": request.session['cart_data_obj'], "totalcartitems": len(request.session['cart_data_obj']), "cart_total_price": cart_total_price})
#     else:
#         return redirect('shopapp:all_categories')

# def cart_items_delete(request):
#     product_id = str(request.GET['id'])
#     if 'cart_data_obj' in request.session:
#         if product_id in request.session['cart_data_obj']:
#             cart_data = request.session['cart_data_obj']
#             del request.session['cart_data_obj'][product_id]
#             request.session['cart_data_obj'] = cart_data

#     cart_total_price = 0
#     if 'cart_data_obj' in request.session:
#         for product_id, item in request.session['cart_data_obj'].items():
#             cart_total_price += int(item['qty']) * float(item['price'])

#     context = render_to_string("shopapp/async/cart-list.html", {"data":request.session['cart_data_obj'], "totalcartitems":len(request.session['cart_data_obj']), "cart_total_price": cart_total_price})
#     return JsonResponse({"data":context, "totalcartitems":len(request.session['cart_data_obj'])})

def SearchView(request):
    query = request.GET.get("q")
    if query:
        products = Product.objects.filter(name__icontains=query).order_by("-created")
    else:
        products=[]
    context = {
        'products':products,
        'query':query
    }
    return render(request, 'shopapp/search.html', context)




