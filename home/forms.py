from django.forms import ModelForm
from .models import transformation
class PictureForm(ModelForm):
    class Meta:
        model = transformation
        fields = ['photo']