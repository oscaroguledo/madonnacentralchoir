from django import forms
from .models import Sheet, Audio, Video

class SheetForm(forms.ModelForm):
    class Meta:
        model = Sheet
        fields = ('title', 'composer','cover', 'type','part_of_calender','part_of_mass','uploader','file' )


class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ('title', 'composer','type', 'part_of_calender', 'part_of_mass', 'uploader', 'file')


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'composer','type', 'part_of_calender', 'part_of_mass', 'uploader', 'file')
