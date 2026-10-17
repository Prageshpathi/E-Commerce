from functools import wraps

from django.shortcuts import redirect


def auth_middleware(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        if not request.session.get('customer'):
            return redirect('login')
        return view_func(request, *args, **kwargs)

    return wrapped_view