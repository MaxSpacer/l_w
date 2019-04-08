from django.template.context_processors import request
from datetime import datetime
from landing.forms import MainForm
from educations.forms import EducationOrderForm

def getting_now_date(request):
    # form_class_page = {
    # '/educations/': EducationOrderForm,
    # '/landing/x': MainForm
    # }
    # # form_class = MainForm
    # for key in form_class_page:
    #     if key in request.path:
    #         print(request.path)
    #         print("sdsdsad----------------------------")
    #         print(form_class_page[key])
    #         form_class = form_class_page[key]

    # if forms_for_page in request.path
    form = MainForm(request.POST or None)
    return locals()
