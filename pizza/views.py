from django.shortcuts import render
from .forms import PizzaForm
from .models import Pizza

# Create your views here.
def home(request):
    return render(request, 'pizza/home.html')
 
def order(request):
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST) # instantiate PizzaForm object with filled data!
        if filled_form.is_valid():
            created_pizza = filled_form.save() # saving pizza in DB
            created_pizza_pk = created_pizza.id # access ID of the order
            note = f"Thanks for your order. Your {filled_form.cleaned_data['size']} {filled_form.cleaned_data['topping1']} and {filled_form.cleaned_data['topping2']} pizza is on its way!"
            new_form = PizzaForm()
        else:
            created_pizza_pk = None
            note = 'Pizza order has failed. Try again.'
        context = {'created_pizza_pk': created_pizza_pk, 'pizzaform': filled_form, 'note': note}
        return render(request, 'pizza/order.html', context)
    else:
        form = PizzaForm()
        context = {'pizzaform': form}
        return render(request, 'pizza/order.html', context)


def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk) # Accessing this order by its PK
    form = PizzaForm(instance=pizza) # Accessing that same form to edit it
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            context = {'pizza': pizza}
            return render(request, 'pizza/edit_success.html', context)
    context = {'pizzaform': form, 'pizza': pizza}
    return render(request, 'pizza/edit_order.html', context)

# def edit_success(request, pk):
#     pizza = Pizza.objects.get(pk=pk)
#     context = {'pizza': pizza}
#     return render(request, 'pizza/edit_success.html', context)