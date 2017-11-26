"""Forms for Events and related entities.

"""

import datetime
from bootstrap3_datetime.widgets import DateTimePicker
from .customwidgets import OurDateTimePicker, ArrayFieldSelectMultiple
from django import forms
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model
from django.forms import Textarea, TextInput, RadioSelect, Select, NumberInput, CheckboxInput, CheckboxSelectMultiple, FileField
from django.contrib.postgres.fields import ArrayField
from datetimewidget.widgets import DateTimeWidget
from tinymce.widgets import TinyMCE
# from django.contrib.staticfiles.templatetags.staticfiles import static


from editorial.models import (
    Organization,
    Project,
    Series,
    Story,
    Event,
)


# ------------------------------ #
#          Event Forms           #
# ------------------------------ #
class EventForm(forms.ModelForm):
    """ Form to create/edit an event. """

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['team'].queryset = Organization.get_org_users(self.request.user.organization)
        self.fields['evt_organization'].queryset = Organization.get_org_collaborators_vocab(self.request.user.organization)
        self.fields['event_type'].empty_label='Event Type'
        self.fields['evt_organization'].empty_label='Select an Organization'
        self.fields['project'].empty_label='Select a Project'
        self.fields['series'].empty_label='Select a Series'
        self.fields['story'].empty_label='Select a Story'


    projects = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        widget=forms.Select,
        required=False,
    )

    series = forms.ModelChoiceField(
        queryset=Series.objects.all(),
        widget=forms.Select,
        required=False,
    )

    stories = forms.ModelChoiceField(
        queryset=Story.objects.all(),
        widget=forms.Select,
        required=False,
    )

    event_date = forms.DateTimeField(
        required=False,
        widget=OurDateTimePicker(
            options={'format': 'YYYY-MM-DD HH:mm'},
            attrs={'id': 'event_eventdate_picker'}
        )
    )

    class Meta:
        model = Event
        fields = [
            'name',
            'text',
            'team',
            'event_type',
            'event_date',
            'venue',
            'evt_organization',
            'project',
            'series',
            'story',
        ]
        widgets = {
            'name': Textarea(attrs={'class': 'form-control', 'rows':2, 'placeholder': 'Name'}),
            'text': Textarea(attrs={'class': 'form-control', 'id':'task-text', 'rows':20, 'placeholder': 'Details'}),
            'team': ArrayFieldSelectMultiple(attrs={'class': 'chosen-select form-control facet-select', 'id':'event-team', 'data-placeholder': 'Team'}),
            'event_type': Select(attrs={'class': 'custom-select', 'id':'task-status'}),
            'evt_organization': Select(attrs={'class': 'custom-select', 'id':'event-organization'}),
            'project': Select(attrs={'class': 'custom-select', 'id':'event-project'}),
            'series': Select(attrs={'class': 'custom-select', 'id':'event-series'}),
            'story': Select(attrs={'class': 'custom-select', 'id':'event-story'}),
            }

    class Media:
        css = {
            'all': ('css/bootstrap-datetimepicker.css', 'css/chosen.min.css')
        }
        js = ('scripts/chosen.jquery.min.js',)