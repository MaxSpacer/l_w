from django.shortcuts import render



def checkout(request):

    return render(request, 'checkout/checkout.html', locals())
