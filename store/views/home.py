from django.shortcuts import render,redirect, HttpResponseRedirect
from store.models.products import Products
from store.models.category import Category
from django.views import View

class Index(View):
    def post(self, request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')

        cart= request.session.get('cart',{})

        if product:
            pid=str(product)
            quantity=cart.get(pid,0)
            if remove:
                if quantity <=1:
                    cart.pop(pid,None)
                else:
                    cart[pid]=quantity-1
            else:
                cart[pid]=quantity+1
            request.session['cart']= cart

        return redirect('homepage')
    def get(self,request):

        products=None
        categories=Category.get_all_categories()
        categoryID=request.GET.get('category')

        if categoryID:
            products=Products.get_all_categories()
        else:
            products=Products.get_all_products()

        data={
            'products':products,
            'categories': categories
        }
        return render(request,'index.html',data)
def store(request):
    return render(request,'store.html')            
                            
                
