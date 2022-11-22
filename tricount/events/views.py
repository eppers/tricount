from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from tricount.events.forms import EventForm
from tricount.events.models import Event


class EventListView(ListView):
    model = Event


class EventCreateView(CreateView):
    model = Event
    success_url = reverse_lazy("events:event_list")

    form_class = EventForm

    def form_valid(self, form):
        event_model = form.save(commit=False)
        event_model.user_id = self.request.user.id
        event_model.save()
        return super().form_valid(form)


class EventUpdateView(UpdateView):
    model = Event
    success_url = reverse_lazy("events:event_list")

    form_class = EventForm


class EventDeleteView(DeleteView):
    model = Event
    success_url = reverse_lazy("events:event_list")
