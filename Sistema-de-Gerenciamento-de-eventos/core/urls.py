from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path("register/", create_user),
    path("send_email/", email_sender),
    path("create-event/", create_event),
    path("get-events/", get_events),
    path("get-event", get_event),
    path("get-event-for-coordinates", get_events_for_coordinates_user),
    path("get-events-for-description", get_events_for_description),
    path("get-events-for-date", get_events_for_init_date),
    path("get-events-for-country", get_events_for_country),
    path("get-events-for-state", get_events_for_state),
    path("get-events-for-city", get_events_for_city),




]
