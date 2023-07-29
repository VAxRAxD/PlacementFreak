from django.forms import ModelForm
from .models import *

class experienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = "__all__"