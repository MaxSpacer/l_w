from django.shortcuts import render
from educations.models import Education
from django.utils import timezone


def education_list(request):

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    # print(request.session.session_key)
    educations = Education.objects.filter(is_active=True, publicated__lte=timezone.now()).order_by('-publicated')
    # print(educations)
    return render(request, 'educations/educations.html', locals())


def education(request, education_id):
    education = Education.objects.get(id=education_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    # print(request.session.session_key)

    return render(request, 'educations/education.html', locals())
