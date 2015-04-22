from core.models import Member
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from core.forms import RegisterForm


@login_required
def index(request):
    """Render the main interface."""
    return render(request, 'core/index.html')


def login_view(request):
    """
    Show the login form and handle them.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('index'))

    else:
        form = AuthenticationForm()

    return render(request, 'core/login.html', {'form': form})


def logout_view(request):
    """Logout and redirect to login form."""
    logout(request)
    return redirect(reverse('login'))


def register(request):
    """
    Show the register form and handle them. If the user already
    is logged in, redirect them to the main interface. If form was
    valid, create a new member using `Member`'s class method `create`
    and redirect them to the main interface.
    """
    if request.user.is_authenticated():
        return redirect(reverse('index'))

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if not Member.objects.get(email=form.cleaned_data['email']):
                member = Member.create(email=form.cleaned_data['email'],
                                       password=form.cleaned_data['password'],
                                       name=form.cleaned_data['name'])
                authenticate(form.cleaned_data['email'], form.cleaned_data['password'])
                login(request, member.user)
                return redirect(reverse('index'))
            else:
                raise

    else:
        form = RegisterForm()

    return render(request, 'core/register.html', {'form': form})
