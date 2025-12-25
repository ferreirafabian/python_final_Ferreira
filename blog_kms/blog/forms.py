from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['imagen', 'kilometros', 'dinero', 'pedidos', 'fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'})
        }
