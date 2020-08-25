from django.shortcuts import render
from .models import *


def show_home(request):
    context = {'numbers': Game.number, 'temporary_number': PlayerGameInfo.temporary_number}
    return render(
        request,
        'home.html',
        context=context,
    )
