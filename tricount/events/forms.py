from django import forms
from django.forms import CheckboxInput
from bootstrap_datepicker_plus.widgets import DateTimePickerInput, TimePickerInput, TimePickerInput
from tricount.events.models import Event


class EventForm(forms.ModelForm):
    started_at = forms.DateTimeField(
        widget=DateTimePickerInput(
            options={
                "showTodayButton": True,
            },
        )
    )
    settle = forms.BooleanField(required=False, widget=CheckboxInput(attrs={"type": "checkbox"}))

    class Meta:
        model = Event
        fields = "label", "started_at", "settle"
