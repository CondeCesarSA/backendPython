from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from apps.user.models import User, Tarjeta
from apps.persona.models import Direccion, Localidad, Provincia, Pais,Telefono
from django import forms
from datetime import datetime

# Get
# mostrar usuario


class HomePageView(ListView):
    # template_name = "user/home.html"
    model = User
# de aca para abajo hay que usarlo en el employee depues
#
# Post
# CREAR  USUARIO


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['fechaNacimiento', 'registrado', 'provincia', 'localidad',
                   'pais', 'direccion', 'nacionalidad', 'telefono', 'tarjeta']
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    calle = forms.CharField(max_length=255)
    cod_area = forms.IntegerField()
    prefijo = forms.IntegerField()
    numero = forms.IntegerField()
    tarjeta = forms.ModelChoiceField(queryset=Tarjeta.objects.all())
    localidad = forms.ModelChoiceField(queryset=Localidad.objects.all())
    provincia = forms.ModelChoiceField(queryset=Provincia.objects.all())
    nacionalidad = forms.ModelChoiceField(queryset=Pais.objects.all())


class CreateUserView(CreateView):
    # template_name = 'user/nuevo.html'  # Si decides usar un template personalizado, descomenta esta línea
    model = User
    form_class = UserForm
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        # Obtener los valores del formulario
        cod_area = form.cleaned_data['cod_area']
        prefijo = form.cleaned_data['prefijo']
        numero = form.cleaned_data['numero']

        pais = form.cleaned_data['nacionalidad']
        localidad = form.cleaned_data['localidad']
        provincia = form.cleaned_data['provincia']

        fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
        calle = form.cleaned_data['calle']
        tarjeta = form.cleaned_data['tarjeta']
        # Crear instancias de los modelos relacionados
        telefono_instance = Telefono(codArea=cod_area, prefijo=prefijo, numero=numero)
        telefono_instance.save()

        direccion_instance = Direccion(calle=calle, localidad=localidad)
        direccion_instance.save()

        # Crear la instancia de User
        user_instance = form.save(commit=False)
        user_instance.fecha_nacimiento = fecha_nacimiento
        user_instance.pais = pais
        user_instance.provincia = provincia
        user_instance.direccion = direccion_instance
        user_instance.telefono = telefono_instance
        user_instance.tarjeta = tarjeta
        user_instance.registrado = datetime.now().date()
        user_instance.save()

        return super().form_valid(form)


# put/ path
# ACTUALIZAR USUARIO
class UpdateUserView(UpdateView):
    # template_name = 'user/user_update_form.html'
    model = User
    form_class = UserForm 
    success_url = reverse_lazy('home')

# delete
# ELIMINAR USUARIO


class DeleteUserView(DeleteView):
    # template_name = 'notas/eliminar.html'
    model = User
    success_url = reverse_lazy('home')
