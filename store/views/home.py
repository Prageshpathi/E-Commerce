from django.shortcuts import render, redirect
from django.views import View

from store.category import Category
from store.products import Products


class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')

        cart = request.session.get('cart', {})

        if product:
            pid = str(product)
            quantity = cart.get(pid, 0)
            if remove:
                if quantity <= 1:
                    cart.pop(pid, None)
                else:
                    cart[pid] = quantity - 1
            else:
                cart[pid] = quantity + 1
            request.session['cart'] = cart

        return redirect('homepage')

    def get(self, request):
        products = None
        categories = Category.get_all_categories()
        category_id = request.GET.get('category')

        if category_id:
            products = Products.get_all_products_by_categoryid(category_id)
        else:
            products = Products.get_all_products()

        data = {
            'products': products,
            'categories': categories,
        }
        return render(request, 'index.html', data)


def store(request):
    return render(request, 'store.html')

