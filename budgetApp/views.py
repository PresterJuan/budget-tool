from django.shortcuts import render
from budgetApp.models import Stuff
from budgetApp.forms import NewCategory

# Create your views here.
def index(request):
    form = NewCategory()
    budget_list = Stuff.objects.order_by('top_name')

    if request.method == "POST":
        form = NewCategory(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            pass
            #print ('error form is invalid')
    return render(request,'budgetApp/index.html', {'stuff': budget_list, 'form':form})
