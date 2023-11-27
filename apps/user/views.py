from  django.views.generic.list import ListView

from apps.user.models import User

# Get
# mostrar usuario

class HomePageView(ListView):
    template_name = "user/home.html"
    model = User

# Post
# CREAR  USUARIO

# put/ path
# ACTUALIZAR USUARIO

# delete
# ELIMINAR USUARIO