from django.shortcuts import render
from .forms import UserNumber
import math
def home(request):
    fact_num_ans = None
    if request.method == "POST":
        form = UserNumber(request.POST)
        num = int(form['num'].value())
        print(num)
        fact_num_ans = math.factorial(num)
        print(fact_num_ans)
    else:
        form = UserNumber()
 
    context = {
        'form':form,
        'fact_num_ans':fact_num_ans
 

    }
    return render(request, "findfactorial/home.html", context)
