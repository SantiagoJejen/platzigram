"""Posts views """

# Djago 
#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView



# Forms

from posts.forms import PostForm
# Models
from posts.models import Post

from django.contrib.auth.models import User

#Utilites 
from datetime import datetime
# Create your views here.



class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 2
    context_object_name = 'posts'

#@login_required
#def list_posts(request):
#    """List existing posts."""
#    posts = Post.objects.all().order_by('-created')
#
#    return render(request, 'posts/feed.html', {'posts': posts})

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context
        

#@login_required
#def create_post(request):
#    """Create new post view."""
#    if request.method == 'POST':
#        form = PostForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect('posts:feed')
#
#    else:
#        form = PostForm()
#
#    return render(
#        request=request,
#        template_name='posts/new.html',
#        context={
#            'form': form,
#            'user': request.user,
#            'profile': request.user.profile
#        }
#    )