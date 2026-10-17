from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from store.customer import Customer
from django.contrib.auth.hashers import check_password


class Login(View):
    return_url = None

    def get(self, request):
        self.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        password=request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                if self.return_url:
                    return HttpResponseRedirect(self.return_url)
                self.return_url = None
                return redirect('homepage')
            error_message = 'Email or Password invalid!!!'
        else:
            error_message = 'Email or Password invalid!!!'

        return render(request, 'login.html', {'error': error_message})

    @staticmethod
    def logout(request):
        request.session.clear()
        return redirect('login')