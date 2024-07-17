# from django import forms
# from .models import ModalContent

# class ModalContentForm(forms.ModelForm):
#     video_file = forms.FileField(required=False)

#     class Meta:
#         model = ModalContent
#         fields = ['title', 'content', 'video_url', 'video_file']

#     def clean(self):
#         cleaned_data = super().clean()
#         video_url = cleaned_data.get('video_url')
#         video_file = cleaned_data.get('video_file')

#         if not video_url and not video_file:
#             raise forms.ValidationError("Please provide either a video URL or upload a video file.")

#         return cleaned_data
from django import forms
from .models import ModalContent

class ModalContentForm(forms.ModelForm):
    video_file = forms.FileField(required=False)

    class Meta:
        model = ModalContent
        fields = ['title', 'content', 'video_url', 'video_file']

    def clean(self):
        cleaned_data = super().clean()
        video_url = cleaned_data.get('video_url')
        video_file = cleaned_data.get('video_file')

        if not video_url and not video_file:
            raise forms.ValidationError("Please provide either a video URL or upload a video file.")

        return cleaned_data





