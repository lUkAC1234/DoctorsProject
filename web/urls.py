from django.urls import path, include
from .views import index, signin, signup, logoutView, profile, edit, Payment, Checkout, video_detail, \
commentDeleteView

app_name = "main"


urlpatterns = [
    path('', index, name="index"),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('logout/', logoutView, name='logout'),
    path('profile/', profile.as_view(), name='profile'),
    path('edit/profile/user/', edit, name='edit'),
    path('payment/', Payment.as_view(), name='payment'),
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('video/detail/<int:id>/', video_detail, name='videodetail'),
    path('comments/delete/<int:pk>/', commentDeleteView.as_view(), name='commentdelete'),
]