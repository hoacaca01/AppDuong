from django import forms
from .models import UserProfile, Street

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'birthdate', 'avatar']

class YourStreetForm(forms.ModelForm):
    class Meta:
        model = Street
        # fields = '__all__'
        fields = ['street_name', 'abstract', 'content', 'image1', 'source_docID', 'type_streetID', 'group_streetID', 'id_address', 'position', 'length', 'width', 'lane_number', 'google_map', 'note', 'street_mapid']