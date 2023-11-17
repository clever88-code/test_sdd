from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import FormView, UpdateView
import asyncio

from django.views import View
# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import Application_forms,ApplicationFormEdit  
from core.models import Application
from django.views import View
from django.contrib.auth.decorators import login_required





class RecordView(FormView):
    template_name = 'record.html'
    form_class = Application_forms
    success_url = '/record'
    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        user_applications = Application.objects.filter(auth_user_id=user_id) 
        form = Application_forms
                
        context = {
            'user_applications': user_applications,
            'form': form,

        }
        return render(request, self.template_name, context)
    


def add_orders(request):
    if request.POST:
        form = Application_forms(data=request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.auth_user_id = request.user.id
            obj.save()

    return redirect('/record/')









