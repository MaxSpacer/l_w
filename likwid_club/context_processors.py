from django.template.context_processors import request
from datetime import datetime
from landing.forms import MainForm

def getting_now_date(request):
    nowDate = datetime.now()
    form = MainForm(request.POST or None)
    return locals()
