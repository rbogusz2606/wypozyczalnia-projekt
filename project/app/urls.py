from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path("", views.cars_view, name = "cars-list"),
    path("car/<int:pk>/", views.carview.as_view(), name="car-detail"),
    path("success", views.SuccessView.as_view(), name="success"),
    path("sendmessage", views.Sendmessage.as_view(), name="car-message"),
    path("register", views.registration, name= "register"),
    path("login", views.sign_in, name = "login"),
    path("logout", views.logoutuser, name = "logout"),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)