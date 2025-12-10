from django.contrib.auth.hashers import make_password, check_password
from functools import wraps
from django.shortcuts import redirect
from apps.Usuario.models import Usuario

def hash_password(raw_password: str) -> str:
    return make_password(raw_password)

def verify_password(raw_password: str, hashed: str) -> bool:
    return check_password(raw_password, hashed)

def get_logged_user(request):
    user_id = request.session.get('usuario_id')
    if not user_id:
        return None
    try:
        return Usuario.objects.get(pk=user_id)
    except Usuario.DoesNotExist:
        return None

def login_required_custom(view_func):
    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        if not get_logged_user(request):
            return redirect('usuario:login')
        return view_func(request, *args, **kwargs)
    return _wrapped

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        usuario = get_logged_user(request)
        if not usuario or not getattr(usuario, 'is_admin', False):
            return redirect('jogos:lista')
        return view_func(request, *args, **kwargs)
    return _wrapped