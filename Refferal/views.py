from django.shortcuts import render, redirect
from Dashboard.models import Refferal
# Create your views here.


def main(request, *args, **kwargs):
    code = str(kwargs.get('ref_code'))
    try:
        refferal = Refferal.objects.get(code=code)
        request.session['ref_refferal'] = refferal.id
        # print('id',refferal.id)
    except:
        pass
    # print(request.session.get_expiry_date())
    return render(request, 'register/dashboard.html', {})