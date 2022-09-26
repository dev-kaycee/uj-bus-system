from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import LoginView, RegisterView, HomeView 

app_name = 'user_auth'
urlpatterns = [
    path('register', RegisterView.as_view(), name='perform_register'),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view(), name='login'),
    path('login', LoginView.as_view(), name='perform_login'),
    path('home', HomeView.as_view(), name='home')
    # path('logout', LogoutView.as_view()),
    # path('users', GetUsers.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)