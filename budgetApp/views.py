from django.shortcuts import render
from budgetApp.models import Stuff
from budgetApp.forms import NewCategory

# Create your views here.
def index(request):
    form = NewCategory()
    budget_list = Stuff.objects.order_by('top_name')

    if request.method == "POST":

        if 'newExpense' in request.POST:
            postData = request.POST
            return render(request,'budgetApp/test.html', {'postData': postData})
            """form = NewCategory(request.POST)
            if form.is_valid():
                form.save(commit=True)
                return index(request)
            else:
                print ('error form is invalid')"""
    return render(request,'budgetApp/index.html', {'stuff': budget_list, 'form':form})

def test(request):
    postData = request
    return render(request,'budgetApp/test.html', {'postData': postData})