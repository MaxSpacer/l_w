from django.template.context_processors import request
from datetime import datetime


def getting_now_date(request):
    nowDate = datetime.now()
    # # Render Some Template with a parameter accesible as date
    # return render(request, 'pages/index.html', {
    #     'date': myDate or 'locals'
    # })
    print(request.session.session_key)
    return locals()
