from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect
from referals.models import *

def ref_session_add(request, referer_id):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    if 'referer' not in request.session:
        request.session['referer'] = referer_id
        print("referal_id_obtained")
    else:
        print("referal_id_already_obtained")
    if 'ref_counted' not in request.session:
        request.session['ref_counted'] = True
        user = User.objects.get(pk=referer_id)
        user.profile.referals_qty += 1
        user.save()
        print("referal_counted")
    else:
        print("referal_id_already_counted")
    return redirect('/')
