from django.shortcuts import render, redirect
from .models import Order, Product
from django.db.models import Sum

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    order = Order.objects.last()
    total_quantity = Order.objects.aggregate(Sum('quantity_ordered'))
    total_quant = total_quantity['quantity_ordered__sum']
    total_amount = Order.objects.aggregate(Sum('total_price'))
    total_amt = total_amount['total_price__sum']
    print("Check1212")
    context = {
        "order": order,
        "total_quant": total_quant,
        "total_amt": total_amt,
    }
    return render(request, "store/checkout.html", context)

def buy(request):
    if request.method == 'POST':
        product_with_id = Product.objects.filter(id=request.POST["id"])
        if len(product_with_id) > 0:
            quantity = int(request.POST["quantity"])
            total_charge = quantity*(float(product_with_id[0].price))
            print("Charging credit card...")
            order = Order.objects.create(quantity_ordered=quantity, total_price=total_charge)
            return redirect('/checkout')
    return redirect('/')