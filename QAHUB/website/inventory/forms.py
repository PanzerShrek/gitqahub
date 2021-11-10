from django.forms import ModelForm
from .models import materialForm


class entryForm(ModelForm):
	class Meta:
		model = materialForm
		fields = '__all__'
