from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('submit-lead', views.submit_lead),
    path('thankyou', views.thanks),
    path('sign_up', views.sign_up),
    path('login-admin', views.adminLogin),
    path('dashboard', views.dashboard),
    path('remove/<int:uid>', views.delete_lead),
    path('get_csv', views.get_csv),
]