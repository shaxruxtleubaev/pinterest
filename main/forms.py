from django.forms import ModelForm
from main.models import Post, Category

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'category',
            'image'
        ]