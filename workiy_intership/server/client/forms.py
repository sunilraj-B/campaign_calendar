from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    week2_backlog = forms.BooleanField(required=False)
    week3_backlog = forms.BooleanField(required=False)
    week4_backlog = forms.BooleanField(required=False)
    class Meta:
        model = Event
        fields = ['name', 'event_name', 'starting_date']
        widgets = {
            'starting_date': forms.SelectDateWidget(),
            'week2_date': forms.SelectDateWidget(),
            'week3_date': forms.SelectDateWidget(),
            'week4_date': forms.SelectDateWidget(),
        }
