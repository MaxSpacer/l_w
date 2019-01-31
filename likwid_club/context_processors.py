from django.template.context_processors import request
from datetime import datetime


def getting_now_date(request):
    nowDate = datetime.now()
    return locals()
