from django.urls import reverse_lazy
from  django.views.generic.list import ListView
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from apps.user.models import User

# Get
# mostrar usuario

class HomePageView(ListView):
    # template_name = "user/home.html"
    model = User
## de aca para abajo hay que usarlo en el employee depues
#
# Post
# CREAR  USUARIO

class CreateUserView(CreateView):
    # template_name = 'user/nuevo.html'
    model = User
    fields = ['apellido', 'dni']
    success_url =reverse_lazy('home')


# put/ path
# ACTUALIZAR USUARIO
class UpdateUserView(UpdateView):
    # template_name = 'user/user_update_form.html'
    model = User
    fields = ['apellido', 'dni']  
    success_url =reverse_lazy('home')

# delete
# ELIMINAR USUARIO

class DeleteUserView(DeleteView):
    # template_name = 'notas/eliminar.html'
    model = User
    success_url = reverse_lazy('home')


    