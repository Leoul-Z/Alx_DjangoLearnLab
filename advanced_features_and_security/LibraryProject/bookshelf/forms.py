from django import forms
from .models import Book

# ---- Secure Search Form ----


class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Search books...'})
    )


# ---- Book Form (for create/edit) ----
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

        # Add widgets for better security and UX
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }
