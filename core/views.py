from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView
from django.template.loader import  render_to_string
from django.core.mail import EmailMessage

from .models import Project, Service, Testimonial,PopUp
from .forms import ContactForm


# Create your views here.
class IndexView(ListView):
    template_name = 'core/index.html'
    model = Project
    paginate_by = 6

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(status=True)
        context['services'] = Service.objects.filter(status=True)
        context['modal'] = PopUp.objects.all().last()
        context['testimonials'] = Testimonial.objects.all()

        return context

class ContactView(TemplateView):
    template_name = 'core/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['form'] = ContactForm()

        return context

    def post(self, request, *args, **kwargs):
        nombre = request.POST.get('name')
        correo = request.POST.get('email')
        asunto = request.POST.get('subject')
        mensaje = request.POST.get('message')
        try:
            body= render_to_string('core/email_content.html', {
                'name':nombre,
                'email':correo,
                'subject':asunto,
                'message':mensaje,

            },)

            email_message=EmailMessage(
                subject='Mensaje star glass ' + asunto,
                body=body,
                from_email=correo,
                to=['contacta@starglass.com.co'],
            )
            email_message.content_subtype='html'
            email_message.send()
            print('Enviado con exito')

        except:
            return redirect(reverse('contact')+ "?fail")

        return redirect(reverse('contact')+"?ok")

class AboutView(TemplateView):
    template_name = 'core/about.html'

class ServiceList(ListView):
    template_name = 'core/services.html'
    model = Service
    context_object_name = 'services'
    paginate_by = 20



def serviceDetail(request,pk):
    template_name = 'core/serviceDetail.html'
    context={}
    query = Project.objects.filter(service=pk)
    if query:
        context['projects'] = Project.objects.filter(service=pk)
    else:
        return redirect(reverse_lazy('index'))

    return render(request,template_name,context)