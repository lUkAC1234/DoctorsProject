from django.urls import path, include
from .views import index, signin, signup, logoutView, profile, edit, Payment, Checkout, \
VideoDetail

app_name = "main"


urlpatterns = [
    path('', index, name="index"),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('logout/', logoutView, name='logout'),
    path('profile/', profile.as_view(), name='profile'),
    path('edit/profile/user', edit, name='edit'),
    path('payment/', Payment.as_view(), name='payment'),
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('video/detail/<int:pk>/<slug:slug>', VideoDetail.as_view(), name='videodetail'),
]