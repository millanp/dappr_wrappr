from django.shortcuts import render
from django.views.generic.edit import FormView
from dappr.forms import RegistrationForm
from django.core.urlresolvers import reverse
from braces.views import FormValidMessageMixin
from django.contrib.auth.models import User
from dappr.models import RegistrationProfile

# Create your views here.
class RegistrationView(FormValidMessageMixin, FormView):
    template_name = 'registration/registration_form.html'
    form_class = RegistrationForm
    success_url = "/"# reverse('login')
    form_valid_message = "This is the form valid message"
    
    def form_valid(self, form):
        user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
        )
        user.set_unusable_password()
        user.is_active = False
        user.save();
        reg_profile = RegistrationProfile.objects.create(user=user)
        reg_profile.send_user_confirmation()
        return super(RegistrationView, self).form_valid(form)