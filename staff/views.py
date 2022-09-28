from django.shortcuts import render
from django.views.generic import TemplateView
from accounts.models import Visitor

# Create your views here.
class Homepage(TemplateView):
    template_name = 'staff_homepage.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        q = self.request.GET.get('search')
        if q:
            visitors = Visitor.objects.filter(first_name__icontains = q)
            context['visitors'] = visitors
            
        return context
