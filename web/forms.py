from django import forms


class CommentForm(forms.Form):
    """Formulário para adicionar comentários no blog."""
    commentary = forms.CharField(max_length=2000, widget=forms.Textarea, help_text='Enter comment about blog here.')
