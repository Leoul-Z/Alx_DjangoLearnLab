from django import forms
from .models import Post
from django import forms
from .models import Comment
from .models import Post, Tag


class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Comma-separated tags")

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        # handle tags
        tag_names = self.cleaned_data["tags"].split(",")
        for name in tag_names:
            name = name.strip()
            if name:
                tag, created = Tag.objects.get_or_create(name=name)
                instance.tags.add(tag)
        return instance


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 3, "placeholder": "Write a comment..."})
        }
