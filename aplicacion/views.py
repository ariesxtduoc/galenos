from django.conf import settings

from django.shortcuts import render

from django.template.loader import get_template

from django.core.mail import EmailMultiAlternatives

# Create your views here.

def index(request):
    return render(request,'index.html')

def mostrar_feriados(request):
    return render(request, 'aplicacion\mostra_feriados.html')

def enviar_correo(request):
    return render(request, 'aplicacion\enviar_correo.html')


def send_email(mail):
    context = {'mail':mail}
    template = get_template('aplicacion\enviar_correo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Un correo de prueba',
        'CodigoFacilito ',
        settings.EMAIL_HOST_USER,
        [mail]
    )

    email.attach_alternative(content, 'text/html')
    email.send()

def enviar_correo(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')

        send_email(mail)
        

    return render(request, 'aplicacion\enviar_correo.html', {})

