from django.forms import ModelForm
from .models import Bb

class BbForm(ModelForm):
    """Форма  BbForm для связи с моделью Bb.
    Служит для внесения новых объявлений на стороне клиента.
    """
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')