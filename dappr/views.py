from django.shortcuts import render
from django.views.generic import edit
from dappr import forms
from django.core.urlresolvers import reverse
from braces.views import FormValidMessageMixin
from dappr.models import RegistrationProfile
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm

# Create your views here.
# class Confirmation
class UserPasswordUpdate(FormValidMessageMixin, edit.UpdateView):
    model = get_user_model()
    template_name = 'registration/user_password_set_form.html'
    form_class = SetPasswordForm
    form_valid_message = "This is the form valid message"
    success_url = "#"
    def get_form_kwargs(self):
        kwgs = edit.UpdateView.get_form_kwargs(self)
        kwgs['user'] = self.object
        # TODO: Find out why you need to delete this
        del kwgs['instance']
        return kwgs
    def form_valid(self, form):
        self.get_registration_profile().send_admin_notification()
        return FormValidMessageMixin.form_valid(self, form)
    def get_object(self, queryset=None):
        return self.get_registration_profile().user
    def get_registration_profile(self):
        return RegistrationProfile.objects.get(confirmation_key=self.kwargs['conf_key'])
class RegistrationForm(FormValidMessageMixin, edit.FormView):
    template_name = 'registration/registration_form.html'
    form_class = forms.RegistrationForm
    success_url = "#"# reverse('login')
    form_valid_message = "This is the form valid message"
    
    def form_valid(self, form):
        user = get_user_model().objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
        )
        user.set_unusable_password()
        user.is_active = False
        user.save();
        reg_profile = RegistrationProfile.objects.create(user=user)
        reg_profile.send_user_confirmation()
        return super(RegistrationForm, self).form_valid(form)