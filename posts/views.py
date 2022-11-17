from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/users/login/")
def order_food(request):
    context = {
        "title": "Order"
    }
    return render(request, "posts/order.html", context=context)
