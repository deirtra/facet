"""Forms for Assets and related entities."""

from django import forms
from django.forms import Textarea, TextInput, Select, Form

from editorial.models import (
    ImageAsset,
    DocumentAsset,
    AudioAsset,
    VideoAsset,
    SimpleImage,
    SimpleDocument,
    SimpleAudio,
    SimpleVideo,
)


# ------------------------------ #
#          Asset Forms           #
# ------------------------------ #

class ImageAssetForm(forms.ModelForm):
    """Upload image to a facet."""

    class Meta:
        model = ImageAsset
        fields = [
            'title',
            'description',
            'attribution',
            'photo',
            'asset_type',
            'keywords',
        ]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Asset Title'}),
            'description': Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
            'attribution': Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Attribution'}),
            'asset_type': Select(attrs={'class': 'form-control'}),
            'keywords': Textarea(
                attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Keywords'}),
        }


class DocumentAssetForm(forms.ModelForm):
    """Upload document to a facet."""

    class Meta:
        model = DocumentAsset
        fields = [
            'title',
            'description',
            'attribution',
            'document',
            'asset_type',
            'keywords',
        ]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Asset Title'}),
            'description': Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
            'attribution': Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Attribution'}),
            'asset_type': Select(attrs={'class': 'form-control'}),
            'keywords': Textarea(
                attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Keywords'}),
        }


class AudioAssetForm(forms.ModelForm):
    """Upload audio to a facet."""

    class Meta:
        model = AudioAsset
        fields = [
            'title',
            'description',
            'attribution',
            'audio',
            'link',
            'asset_type',
            'keywords',
        ]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Asset Title'}),
            'description': Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
            'attribution': Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Attribution'}),
            'link': TextInput(attrs={'class': 'form-control', 'placeholder': 'Link'}),
            'asset_type': Select(attrs={'class': 'form-control'}),
            'keywords': Textarea(
                attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Keywords'}),
        }


class VideoAssetForm(forms.ModelForm):
    """Upload video to a facet."""

    class Meta:
        model = VideoAsset
        fields = [
            'title',
            'description',
            'attribution',
            'video',
            'link',
            'asset_type',
            'keywords',
        ]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Asset Title'}),
            'description': Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
            'attribution': Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Attribution'}),
            'link': TextInput(attrs={'class': 'form-control', 'placeholder': 'Link'}),
            'asset_type': Select(attrs={'class': 'form-control'}),
            'keywords': Textarea(
                attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Keywords'}),
        }


# -------------------------------#
#    Organization Library Forms
# -------------------------------#

class LibraryImageAssociateForm(Form):
    """ Form for adding existing library images to a facet. """

    def __init__(self, *args, **kwargs):
        org = kwargs.pop("organization")
        super(LibraryImageAssociateForm, self).__init__(*args, **kwargs)
        self.fields['images'] = forms.ModelMultipleChoiceField(
            queryset=org.imageasset_set.all(),
            required=False)


class LibraryDocumentAssociateForm(Form):
    """ Form for adding existing library documents to a facet. """

    def __init__(self, *args, **kwargs):
        org = kwargs.pop("organization")
        super(LibraryDocumentAssociateForm, self).__init__(*args, **kwargs)
        self.fields['documents'] = forms.ModelMultipleChoiceField(
            queryset=org.documentasset_set.all(),
            required=False)


class LibraryAudioAssociateForm(Form):
    """ Form for adding existing library audio to a facet. """

    def __init__(self, *args, **kwargs):
        org = kwargs.pop("organization")
        super(LibraryAudioAssociateForm, self).__init__(*args, **kwargs)
        self.fields['audio'] = forms.ModelMultipleChoiceField(
            queryset=org.audioasset_set.all(),
            required=False)


class LibraryVideoAssociateForm(Form):
    """ Form for adding existing library video to a facet. """

    def __init__(self, *args, **kwargs):
        org = kwargs.pop("organization")
        super(LibraryVideoAssociateForm, self).__init__(*args, **kwargs)
        self.fields['video'] = forms.ModelMultipleChoiceField(
            queryset=org.videoasset_set.all(),
            required=False)


# ------------------------------ #
#          Simple Forms          #
# ------------------------------ #

class SimpleImageForm(forms.ModelForm):
    """Upload a simple image."""

    class Meta:
        model = SimpleImage
        fields = [
            'title',
            'description',
            'photo',
        ]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
        }


class SimpleDocumentForm(forms.ModelForm):
    """Upload a simple document."""

    class Meta:
        model = SimpleDocument
        fields = [
            'title',
            'description',
            'document',
        ]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
        }


class SimpleAudioForm(forms.ModelForm):
    """Upload a simple audio file."""

    class Meta:
        model = SimpleAudio
        fields = [
            'title',
            'description',
            'audio',
            'link',
        ]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
            'link': TextInput(attrs={'class': 'form-control', 'placeholder': 'Link'}),

        }


class SimpleVideoForm(forms.ModelForm):
    """Add a simple video."""

    class Meta:
        model = SimpleVideo
        fields = [
            'title',
            'description',
            'link',
        ]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
            'link': TextInput(attrs={'class': 'form-control', 'placeholder': 'Link'}),

        }