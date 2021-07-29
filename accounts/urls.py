from django.urls import path

from accounts.views import CreateUserView, LoginView


urlpatterns = [
    path('', LoginView.as_view(), name='login_url'),
    path('register/', CreateUserView.as_view(), name='register_url')

]