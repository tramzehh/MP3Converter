from django.forms import ModelForm
from convert.models import Link

class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ('url',)