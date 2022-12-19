from django import forms
from .models import Material, PostulacionInstr
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class MaterialForm (forms.ModelForm):
    class Meta:
        model = Material 
        fields = ("idMaterial","nombreMaterial","descripcionMaterial","stock")
    def clean(self):
        print(self.cleaned_data)
        return self.cleaned_data



class PostulacionInstrForm (forms.ModelForm):
    class Meta:
        model = PostulacionInstr
        fields = ("idPostulacion","nombres","apellidos","correo","direccion","rut", "taller", "descripcion")
    def clean(self):
        
        print(self.cleaned_data)
        return self.cleaned_data
        

class CustomerUserCreationForm (UserCreationForm):
   class Meta:
    model = User
    fields=['username',"first_name","last_name","email","password1","password2"]
class ModificarUsuario (ModelForm):
   class Meta:
    model = User
    fields=['username',"first_name","last_name","email"]

class CrearCuentaAdmin (UserCreationForm):
   class Meta:
    model = User
    fields=['username',"first_name","last_name","email","is_superuser","password1","password2"]

class CrearCuentaInstructor (UserCreationForm):
   class Meta:
    model = User
    fields=['username',"first_name","last_name","email","is_staff","password1","password2"]

