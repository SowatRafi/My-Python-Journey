from django import forms


class ToDoListForm(forms.Form):
    text = forms.CharField(max_length=45,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Enter todo e.g Next target...',
                                      'aria-label': 'Todo', 'aria-describeby': 'add-btn'}
                           ))
