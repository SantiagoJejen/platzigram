"""Users views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.views.generic import DetailView, FormView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post
# Forms
from users.forms import SignupForm


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

class LoginView(auth_views.LoginView):
    """Login view."""
    template_name = 'users/login.html'
    redirect_authenticated_user = True

#def login_view(request):
#    """Login view."""
#    if request.method == 'POST':
#        username = request.POST['username']
#        password = request.POST['password']
#        user = authenticate(request, username=username, password=password)
#        if user:
#            login(request, user)
#            return redirect('posts:feed')
#        else:
#            return render(request, 'users/login.html', {'error': 'Invalid username and password'})
#
#    return render(request, 'users/login.html')
#

class SignupView(FormView):
    """ Users signup view. """
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)

#def signup(request):
#    """Sign up view."""
#    if request.method == 'POST':
#        form = SignupForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('users:login')
#    else:
#        form=SignupForm() 
#    return render(
#        request = request, 
#        template_name = 'users/signup.html',
#        context = {
#            'profile': Profile,
#            'user': request.user,
#            'form': form}
#        )
#

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""

    template_name = 'users/logged_out.html'
#@login_required
#def logout_view(request):
#    """Logout a user."""
#    logout(request)
#    return redirect('users:login')

class UpdateProfile(LoginRequiredMixin, UpdateView):
    """Update a user's profile view."""
    template_name='users/update_profile.html'
    model= Profile
    fields = ['website', 'phone_number', 'biography', 'picture']

    def get_object(self):
        """ Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile"""
        username = self.object.user.username
        return reverse('users:detail', kwargs = {'username':username})





#@login_required
#def update_profile(request):
#    """Update a user's profile view."""
#    profile = request.user.profile
#
#    if request.method == 'POST':
#        form = ProfileForm(request.POST, request.FILES)
#        if form.is_valid():
#            data = form.cleaned_data
#
#            profile.website = data['website']
#            profile.phone_number = data['phone_number']
#            profile.biography = data['biography']
#            profile.picture = data['picture']
#            profile.save()
#            url = reverse('users:detail', kwargs={'username': request.user.username})
#            return redirect(url)
#            
#
#    else:
#        form = ProfileForm()
#
#    return render(
#        request=request,
#        template_name='users/update_profile.html',
#        context={
#            'profile': profile,
#            'user': request.user,
#            'form': form
#        }
#    )
#