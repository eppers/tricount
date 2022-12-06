from django.urls import path
from tricount.events.views import EventListView, EventCreateView, EventUpdateView, EventDeleteView
app_name = "events"
urlpatterns = [
    path("", EventListView.as_view(), name="event_list"),
    path("add/", EventCreateView.as_view(), name="event_add"),
    path("<int:pk>/", EventUpdateView.as_view(), name="event_update"),
    path("<int:pk>/delete/", EventDeleteView.as_view(), name="event_delete"),
]
