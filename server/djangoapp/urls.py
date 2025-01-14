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
    path(route='reviews/dealer/<int:dealer_id>', view=views.get_dealer_reviews, name='dealer_details'),

    # path for add a review view
    path(route='add_review', view=views.add_review, name='add_review'),

    #path for get_dealerships
    path(route='get_dealers/', view=views.get_dealerships, name='get_dealers'),
    path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),

    #path for dealer details
    path(route='dealer/<int:dealer_id>', view=views.get_dealer_details, name='dealer_details'),

    # path for get_cars
    path(route='get_cars', view=views.get_cars, name ='getcars'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
