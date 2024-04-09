from django import forms



DIFFIC__CHOICES = (
    ('#1', 'Easy'),
    ('#2', 'Medium'),
    ('#3', 'Intermediate'),
    ('#4', 'Hard')
)


class RecipesSearchForm(forms.Form):
    recipe_diff = forms.ChoiceField(choices=DIFFIC__CHOICES)
   