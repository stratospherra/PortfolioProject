from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, View, UpdateView
from .forms import SignUpForm
from .models import Profile
from ..Portfolios.models import Portfolio
from django.contrib.auth import login


# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('index')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # Save the user object to the database
        response = super().form_valid(form)

        # Get the newly created user object
        user = User.objects.get(username=form.cleaned_data.get('username'))
        # Create a Profile object for the new user
        Profile.objects.create(user=user)
        login(self.request, user)
        return response


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'registration/profile.html'
    context_object_name = 'profile_detailed'
    slug_field = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolios'] = Portfolio.objects.filter(profile=context['object'])
        return context


class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'registration/update_profile.html'
    fields = '__all__'
    success_url = '/'

