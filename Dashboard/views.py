from django.shortcuts import render
from Users.models import CustomUser
from .models import Refferal

# Create your views here.
def Dashboard(request):
    dash = CustomUser.objects.all()
    ref = Refferal.objects.get(user=request.user)
    # my_resc =ref
    link = Refferal.objects.all()


    context = {
        # 'my_resc': my_resc,
        'link': link,
        'ref' : ref
    }
    return render(request, 'register/dashboard.html', context)