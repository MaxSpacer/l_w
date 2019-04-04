from django.shortcuts import render
from .models import MemberPreference, Bill

# Create your views here.
def hall(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    # investions = investion.objects.filter(is_active=True, publicated__lte=timezone.now()).order_by('-publicated')
    preferences = MemberPreference.objects.filter(is_active=True).order_by('-order')
    broker_list = Bill.objects.filter(is_active=True).order_by('-order')

    return render(request, 'hall/hall.html', locals())
