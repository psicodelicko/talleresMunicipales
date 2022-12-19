from django.shortcuts import render
from .form import MaterialForm, CustomerUserCreationForm, PostulacionInstrForm, CrearCuentaAdmin,CrearCuentaInstructor
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, render
from django.core.mail import EmailMessage
from core.models import Material, PostulacionInstr

# Create your views here.


def home(request):
    return render(request, 'core/home.html')


def Form_Inscripcion_Taller(request):
    return render(request, 'core/Form_Inscripcion_Taller.html')


def Form_Instructor_Taller(request):
    datos = {
        'form': PostulacionInstrForm()
    }
    if request.method == 'POST':
        formmulario = PostulacionInstrForm(request.POST)
        if formmulario.is_valid:
            formmulario.save()
            messages.success(request, "Postulación registrada correctamente")
            nombre = formmulario.cleaned_data['nombres']+ formmulario.cleaned_data['apellidos']
            email = formmulario.cleaned_data['correo']
            print(email)
            contenido = "Su postulación como instructor fue enviada correctamente, en un plazo máximo de 36 horas responderemos a su solicitud.\n\n\n Atte.,\n Dirección de Recursos Humanos. \n Puente Alto." 
            
            email = EmailMessage("Municipalidad de Puente Alto",
                                 "Hola! {} :\n\n {}".format(nombre, contenido),
                                 '',
                                 [email],
                                 reply_to=[email])
            email.send()
            datos['mensaje'] = "Guardados Correctamente"
            return redirect(to="home")

    return render(request, 'core/Form_Instructor_Taller.html', datos)


def Ins_Taller(request):
    material = Material.objects.all()
    datos = {
        'material': material
    }
    return render(request, 'core/Ins_Taller.html', datos)


def Admin_Taller(request):
    material = Material.objects.all()
    datos = {
        'material': material
    }
    return render(request, 'core/Admin_Taller.html', datos)


def Form_Evaluacion(request):
    return render(request, 'core/Form_Evaluacion.html')


def Admin_General(request):
    material = Material.objects.all()
    datos = {
        'material': material
    }
    return render(request, 'core/Admin_General.html', datos)


def crear_Taller(request):
    return render(request, 'core/crear_Taller.html')


def crear_Material(request):
    datos = {
        'form': MaterialForm()
    }
    if request.method == 'POST':
        formmulario = MaterialForm(request.POST)
        if formmulario.is_valid:
            formmulario.save()
            messages.success(request, "Material registrado correctamente")
            datos['mensaje'] = "Guardados Correctamente"
            return redirect(to="Admin_General")

    return render(request, 'core/Crear_Material.html', datos)


def Admin_Perfil(request):
    material = Material.objects.all()
    datos = {
        'material': material
    }
    return render(request, 'core/Admin_Perfil.html', datos)


def Admin_Muni(request):
    material = Material.objects.all()
    datos = {
        'material': material
    }
    return render(request, 'core/Admin_Muni.html', datos)


def Admin_Pago(request):
    material = Material.objects.all()
    datos = {
        'material': material
    }
    return render(request, 'core/Admin_Pago.html', datos)


def Admin_Postulacion(request):
    postulacion = PostulacionInstr.objects.all()
    datos = {
        'postulacion': postulacion
    }
    return render(request, 'core/Admin_Postulacion.html', datos)


def Admin_Cliente(request):
    material = Material.objects.all()
    datos = {
        'material': material
    }
    return render(request, 'core/Admin_Cliente.html', datos)


def Admin_Instructor(request):
    material = Material.objects.all()
    datos = {
        'material': material
    }
    return render(request, 'core/Admin_Instructor.html', datos)


def Admin_Banner_Promocion(request):
    material = Material.objects.all()
    datos = {
        'material': material
    }
    return render(request, 'core/Admin_Banner.html', datos)


def Tus_Talleres(request):
    material = Material.objects.all()
    datos = {
        'material': material
    }
    return render(request, 'core/Tus_Talleres.html', datos)


def Eliminar_Material(request, id):
    material = Material.objects.get(idMaterial=id)
    material.delete()
    material = Material.objects.all()
    messages.success(request, "Material eliminado correctamente")
    datos = {
        'material': material
    }
    return render(request, 'core/Admin_General.html', datos)


def EvaluarPostulacion(request, id):
    postulacionInstr = PostulacionInstr.objects.get(idPostulacion=id)
    postulacionInstr.estado = "Rechazada"
    postulacionInstr.save()
    nombre = postulacionInstr.nombres+" "+postulacionInstr.apellidos
    email = postulacionInstr.correo
    print(email)
    contenido = "Junto con saludar, le informamos que su postulación en esta oportunidad no fue aprobada.\n\n\n Atte.,\n Dirección de Recursos Humanos. \n Puente Alto."
    email = EmailMessage("Municipalidad de Puente Alto",
                         "Hola! {} :\n\n {}".format(nombre, contenido),
                         '',
                         [email],
                         reply_to=[email])
    email.send()
    postulacionInstr = PostulacionInstr.objects.all()
    messages.success(request, "Postulación no aprobada correctamente")
    datos = {
        'postulacionInstr': postulacionInstr
    }
    return redirect(to="Admin_Postulacion")


def AceptarPostulacion(request, id):
    postulacionInstr = PostulacionInstr.objects.get(idPostulacion=id)
    postulacionInstr.estado = "Aceptada"
    postulacionInstr.save()
    nombre = postulacionInstr.nombres+" "+postulacionInstr.apellidos
    email = postulacionInstr.correo
    print(email)
    contenido = "¡¡¡Le informamos que su postulación fue aceptada!!!\n\n Para continuar con el proceso, dirigase a nuestras oficinas en:\n  Av. Concha y Toro 1820, 8152857 Puente Alto, Región Metropolitana. \n\n\n ¡Estamos ansiosos de trabajar trabajar con usted! \n\n\n Atte.,\n Dirección de Recursos Humanos. \n Puente Alto."
    email = EmailMessage("Municipalidad de Puente Alto",
                         "Hola! {} :\n\n {}".format(nombre, contenido),
                         '',
                         [email],
                         reply_to=[email])
    email.send()
    postulacionInstr = PostulacionInstr.objects.all()
    messages.success(request, "Postulación evaluada correctamente")
    return redirect(to="Admin_Postulacion")


def Modificar_Material(request, id):
    material = Material.objects.get(idMaterial=id)
    datos = {
        'form': MaterialForm(instance=material)
    }
    if request.method == 'POST':
        formulario = MaterialForm(data=request.POST, instance=material)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto modificado correctamente")
            return redirect(to="Admin_General")
        datos = {
            'form': MaterialForm(instance=material),
            'mensaje': "Modificado correctamente"
        }
    return render(request, 'core/Modificar_Material.html', datos)


def Validar_Postulacion(request, id):
    postulacionInstr = PostulacionInstr.objects.get(idPostulacion=id)
    datos = {
        'form': PostulacionInstrForm(instance=postulacionInstr)
    }
    if request.method == 'POST':
        formulario = PostulacionInstrForm(
            data=request.POST, instance=postulacionInstr)
        if formulario.is_valid():
            postulacionInstr.estado = "aceptada"
            postulacionInstr.save()
            formulario.save()
            messages.success(request, "Postulación aceptada")
            nombre = postulacionInstr.nombres+" "+postulacionInstr.apellidos
            email = postulacionInstr.correo
            print(email)
            contenido = "¡¡¡Le informamos que su postulación fue aceptada!!!\n\n Para continuar con el proceso, dirigase a nuestras oficinas en:\n  Av. Concha y Toro 1820, 8152857 Puente Alto, Región Metropolitana. \n\n\n ¡Estamos ansiosos de trabajar trabajar con usted! \n\n\n Atte.,\n Dirección de Recursos Humanos. \n Puente Alto."

            # email=EmailMessage("Mensaje de app Django",
            # "Estimad@ {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre, email, contenido),
            # '',
            email = EmailMessage("Mensaje de app Django",
                                 "Hola! {} :\n\n {}".format(nombre, contenido),
                                 '',
                                 [email],
                                 reply_to=[email])

            email.send()
            return redirect(to="Admin_Postulacion")

        datos = {
            'form': PostulacionInstrForm(instance=postulacionInstr),
            'mensaje': "Correo enviado correctamente"
        }
    return render(request, 'core/Validar_Postulacion.html', datos)


def registro(request):
    data = {
        'form': CustomerUserCreationForm
    }
    if request.method == 'POST':
        formulario = CustomerUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Te has registrado correctamente")
            user = authenticate(
                username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)


def Ver_Material(request, id):
    material = Material.objects.get(idMaterial=id)
    datos = {
        'form': MaterialForm(instance=material)
    }
    if request.method == 'POST':
        formulario = MaterialForm(data=request.POST, instance=material)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto modificado correctamente")
            return redirect(to="Admin_General")
        datos = {
            'form': MaterialForm(instance=material),
            'mensaje': "Modificado correctamente"
        }
    return render(request, 'core/Ver_Material.html',datos)


def Registro_Cuenta_Admin(request):
    data = {
        'form': CrearCuentaAdmin
    }
    if request.method == 'POST':
        formulario = CrearCuentaAdmin(data=request.POST)
        if formulario.is_valid():
            formulario.cleaned_data['IS_STAFF']=0
            formulario.save()
            messages.success(request, "Cuenta creada correctamente")
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'core/Registro_Cuenta_Admin.html', data)


def Registro_Cuenta_Instructor(request):
    data = {
        'form': CrearCuentaInstructor
    }
    if request.method == 'POST':
        formulario = CrearCuentaInstructor(data=request.POST)
        if formulario.is_valid():
            formulario.cleaned_data['IS_SUPERUSER']=0
            formulario.cleaned_data['IS_STAFF']=1
            formulario.save()
            messages.success(request, "Cuenta creada correctamente")
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'core/Registro_Cuenta_Instructor.html', data)   