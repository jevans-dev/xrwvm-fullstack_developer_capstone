# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration

    # path for login and logout
    path(route='login', view=views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),

    # path for dealer reviews view

    # path for add a review view
    # path for get_cars
    path(route='get_cars', view=views.get_cars, name ='getcars'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
