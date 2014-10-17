from django.shortcuts import render
from django.views.generic import FormView

from .forms import SendSMSForm

# Create your views here.

class AppIndexView(FormView):
    """
    Main/Home view
    """

    template_name = 'index.html'
    form_class = SendSMSForm
    success_url = '/'


    def form_valid(self, form):

        form.send_sms_message()

        return super(AppIndexView, self).form_valid(form)




