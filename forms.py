from django import forms
from book.models import Book 

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'genre', 'isbn', 'publication_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter book title'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',  # put class name as string
                'placeholder': 'Enter author name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter book description'
            }),
            'genre': forms.Select(attrs={  # 'Select' with capital S
                'class': 'form-control'
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter ISBN'
            }),
            'publication_date': forms.DateInput(attrs={  # field name is lowercase here
                'class': 'form-control',  # fixed typo 'forms-comtrol' -> 'form-control'
                'type': 'date'
            }),
        }