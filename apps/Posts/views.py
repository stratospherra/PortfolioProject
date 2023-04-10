from .forms import PostForm
from .models import Post
from django.views.generic import CreateView, ListView

from ..Portfolios.models import Portfolio
from ..Users.models import Profile


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        profile = Profile.objects.get(user=self.request.user)
        data['portfolios'] = Portfolio.objects.filter(profile=profile)
        return data


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
