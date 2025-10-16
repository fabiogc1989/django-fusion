import math

from django.contrib import messages
from django.views.generic import FormView
from django.urls import reverse_lazy

from .forms import ContactForm
from .models import Service, Employee, Feature


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.order_by('?').all()
        context['employees'] = Employee.objects.order_by('?').all()

        features = Feature.objects.order_by('?').all()
        
        left_features = features[:math.ceil(Feature.objects.count()/2)]
        for position, lf in enumerate(left_features, start = 1):
            lf.delay = f'{position * 0.3:.1f}s'
        context['left_features'] = left_features
        
        right_features = features[math.ceil(Feature.objects.count()/2):]
        for position, rf in enumerate(right_features, start = 1):
            rf.delay = f'{position * 0.3:.1f}s'
        context['right_features'] = right_features
        
        return context
    

    def form_valid(self, form):
        form.send_mail()
        messages.success(request= self.request, message='E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form)


    def form_invalid(self, form):
        messages.error(request= self.request, message='Erro ao enviar um e-mail')
        return super(IndexView, self).form_valid(form)
