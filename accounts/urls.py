from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (HomePageView,
                    SignUpView,
                    )

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),

]
