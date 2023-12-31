from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView
from django.views.generic.edit import FormView
from .forms import RegistrationForm, LoginForm, AccountForm, VideosForm, CommentsForm
from .models import UserModel, VideosModel, Commentsmodel
from django.core.exceptions import ValidationError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.db.models import Q
from django.urls import reverse_lazy
def index(request):
    if request.user.is_authenticated:
        template_name = "pages/index.html"
        videos = VideosModel.objects.all()
        comments = Commentsmodel.objects.all()
        search = request.GET.get('search', '')
        if search: videos = videos.filter(Q(name__icontains=search))
        return render(request, template_name, context={
            'videos': videos,
            'comments': comments,
        })
    else:
        return redirect("main:signin")
    
def video_detail(request, id):
    template_name = 'pages/videodetail.html'
    video = VideosModel.objects.get(id=id)
    form = CommentsForm
    if request.method == "POST":
        form = CommentsForm(data=request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.post = video
            data.user = request.user
            data.save()
            detail_url = reverse('main:videodetail', args=[video.id])
            return redirect(detail_url)
    return render(request, template_name, context={
        'video': video,
        'comment_form': form,
    })

class commentDeleteView(LoginRequiredMixin, DeleteView):
    model = Commentsmodel
    template_name = 'pages/commentdelete.html'
    success_url = reverse_lazy('main:index')  # Change this to your home URL

    def get_success_url(self):
        post_id = self.object.post_id
        detail_url = reverse('main:videodetail', args=[post_id])  # Adjust the URL name
        return detail_url

def signup(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('main:signup')
    else:
        template_name = 'pages/signup.html'
        form_registration = RegistrationForm()
        if request.method == 'POST':
            form_registration = RegistrationForm(data=request.POST, files=request.FILES)
            if form_registration.is_valid():
                del form_registration.cleaned_data['confirm_password']
                user_registration = UserModel(
                    username=form_registration.cleaned_data['username'],
                    password=make_password(form_registration.cleaned_data['password']),
                    email=form_registration.cleaned_data['email']
                )
                user_registration.save()
                return redirect('main:signin')
        return render(request, template_name, context={
            'form': form_registration
        })


def signin(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('main:signin')
    else:
        template_name = 'pages/signin.html'
        form_login = LoginForm()
        if request.method == 'POST':
            form_login = LoginForm(data=request.POST)
            if form_login.is_valid():
                user_login = authenticate(
                    username=form_login.cleaned_data['username'],
                    password=form_login.cleaned_data['password']
                )
                if user_login is not None:
                    login(request, user_login)
                    return redirect('main:index')
                form_login.add_error('password', 'Username or password is incorrect')

        return render(request, template_name, context={
            'form': form_login
        })

def logoutView(request):
    logout(request)
    return redirect("main:signin")

class profile(LoginRequiredMixin, TemplateView):
    template_name = 'pages/profile.html'


@login_required()
def edit(request):
    form = AccountForm
    template_name = 'pages/edit.html'
    if request.method == 'POST':
        form = AccountForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            user = get_object_or_404(UserModel, id=request.user.id)
            form.save()
            return redirect('main:profile')
    return render(request, template_name, context={
        'form': form
    })


class Payment(LoginRequiredMixin, TemplateView):
    template_name = 'pages/payment.html'

class Checkout(LoginRequiredMixin, TemplateView):
    template_name = 'pages/checkout.html'