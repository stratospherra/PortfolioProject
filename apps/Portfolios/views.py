from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, DetailView, CreateView
from .models import Portfolio
from ..Posts.models import Post
from ..Users.forms import SignUpForm
from ..Users.models import Profile
from .forms import PortfolioForm


class HomePortfolioListView(ListView):
    model = Portfolio
    template_name = 'index.html'
    context_object_name = 'portfolios'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SignUpForm()
        context['form_login'] = AuthenticationForm()
        return context


class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio_detailed.html'
    context_object_name = 'portfolio_detailed'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(portfolio=context['object'])
        return context


class PortfolioCreateView(CreateView):
    model = Portfolio
    form_class = PortfolioForm
    template_name = 'add_portfolio.html'
    # fields = '__all__'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profiles'] = Profile.objects.filter(user=self.request.user)
        return context
