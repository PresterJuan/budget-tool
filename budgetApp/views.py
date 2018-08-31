from django.shortcuts import render
from budgetApp.models import Stuff
from budgetApp.forms import NewCategory



# Create your views here.
def index(request):
    form = NewCategory()
    budget_list = Stuff.objects.order_by('top_name')
    amount_budgeted = 0
    amount_spent = 0
    income = 4693
    for i in budget_list:
        amount_budgeted += i.budgeted
        amount_spent += i.actual
    budgeted_saved = income - amount_budgeted
    amount_saved = (amount_budgeted-amount_spent)


    if request.method == "POST":

        #postData = request.POST
        #return render(request,'budgetApp/test.html', {'postData': postData})

        if 'newExpense' in request.POST:
            category = request.POST["Add"]#category you want to add the expense to
            amount_spent = int(request.POST["newExpense"])
            category_info = Stuff.objects.get(top_name=category)
            current_spent = int(category_info.actual)
            current_spent += amount_spent
            category_info.actual = current_spent
            category_info.save()
            form = NewCategory()
            budget_list = Stuff.objects.order_by('top_name')
            amount_budgeted = 0
            amount_spent = 0
            for i in budget_list:
                amount_budgeted += i.budgeted
                amount_spent += i.actual
            budgeted_saved = income - amount_budgeted
            amount_saved = (income-amount_spent)
            return render(request,'budgetApp/index.html', {'stuff': budget_list, 'form':form, 'budgeted_saved':int(budgeted_saved),'amount_budgeted':int(amount_budgeted), 'amount_spent':int(amount_spent), 'amount_saved':int(amount_saved)})
            #old method of testing below
            #postData = category_info
            #return render(request,'budgetApp/test.html', {'postData': postData})

        if "newCategory" in request.POST:
            form = NewCategory(request.POST)
            if form.is_valid():
                form.save(commit=True)
                form = NewCategory()
                budget_list = Stuff.objects.order_by('top_name')
                amount_budgeted = 0
                amount_spent = 0
                for i in budget_list:
                    amount_budgeted += i.budgeted
                    amount_spent += i.actual
                budgeted_saved = income - amount_budgeted
                amount_saved = (income-amount_spent)
                return render(request,'budgetApp/index.html', {'stuff': budget_list, 'form':form, 'budgeted_saved':int(budgeted_saved),'amount_budgeted':int(amount_budgeted), 'amount_spent':int(amount_spent), 'amount_saved':int(amount_saved)})
            else:
                print ('error form is invalid')
    return render(request,'budgetApp/index.html', {'stuff': budget_list, 'form':form, 'budgeted_saved':int(budgeted_saved),'amount_budgeted':int(amount_budgeted), 'amount_spent':int(amount_spent), 'amount_saved':int(amount_saved)})

def test(request):
    budget_list = Stuff.objects.order_by('top_name')
    postData = []
    for i in budget_list:
        postData.append(i.budgeted)
    return render(request,'budgetApp/test.html', {'postData': postData})