from django import forms
from .models import Pizza # to refer to this model in the "Meta" class inside our new form

''' ModelForm is a helper class allowing us to create a Form class from a Django model. The generated Form class will have a form field for every model field specified '''

class PizzaForm(forms.ModelForm):

    # size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)

    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {'topping1': 'Topping 1', 'topping2': 'Topping 2'}



# class MultiplePizzaForm(forms.Form):
#     number = forms.IntegerField(min_value=2, max_value=6)



# #### without ModelForm, older way:
# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label="Topping 1", max_length=100)
#     topping2 = forms.CharField(label="Topping 2", max_length=100)
#     size = forms.ChoiceField(label="Size", choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])