from django.contrib.auth.models import User
from django.shortcuts import redirect


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
        user = User.objects.get(pk=referer_id)
        user.profile.referals_qty += 1
        print(user.profile.referals_qty)
        user.profile.save()
        request.session['ref_counted'] = True
        print("referal_counted")
    else:
        print("referal_id_already_counted")
    return redirect('/')
