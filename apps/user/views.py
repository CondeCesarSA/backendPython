from django.urls import reverse_lazy
from  django.views.generic.list import ListView
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from apps.user.models import User
from apps.persona.models import Direccion, Localidad
from django import forms

# Get
# mostrar usuario

class HomePageView(ListView):
    # template_name = "user/home.html"
    model = User
## de aca para abajo hay que usarlo en el employee depues
#
# Post
# CREAR  USUARIO
class TuFormularioEspecializado(forms.ModelForm):
    # Campos para el modelo User
    nombre = forms.CharField(max_length=255)
    apellido = forms.CharField(max_length=255)
    dni = forms.CharField(max_length=20)
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    nacionalidad = forms.CharField(max_length=255)
    
    # Nuevos campos para la dirección
    calle = forms.CharField(max_length=255)
    localidad = forms.ModelChoiceField(
        queryset=Localidad.objects.all(),
        empty_label="Selecciona una localidad",
    )

    class Meta:
        model = User
        fields = [
            'nombre', 'apellido', 'dni', 'fecha_nacimiento', 'nacionalidad',
            'calle', 'localidad' 
        ]


class CreateUserView(CreateView):
    # template_name = 'user/nuevo.html'  # Si decides usar un template personalizado, descomenta esta línea
    model = User
    form_class = TuFormularioEspecializado
    success_url = reverse_lazy('home')



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


    