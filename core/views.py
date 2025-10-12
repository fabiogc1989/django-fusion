import math

from django.views.generic import TemplateView

from .models import Service, Employee, Feature


class IndexView(TemplateView):
    template_name = 'index.html'

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
        