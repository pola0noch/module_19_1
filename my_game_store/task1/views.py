from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import Buyer, Game

# Create your views here.

def menu_view(request):
    return render(request, 'fourth_task/menu.html')

def games_view(request):
    games = Game.objects.all()

    context = {
        'games': games
    }
    return render(request, 'fourth_task/games.html', context)

def cart_view(request):
    return render(request, 'fourth_task/cart.html')


def registration(request):
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        # Устанавливаем значение по умолчанию для balance
        balance = request.POST.get('balance')
        if balance is None or balance == '':
            balance = 0.0  # Устанавливаем значение по умолчанию

        if not Buyer.objects.filter(name=username).exists():
            if password == repeat_password:
                if age >= 18:
                    Buyer.objects.create(
                        name=username,
                        password=password,
                        age=age,
                        balance=balance
                    )
                    return HttpResponse(f'Регистрация прошла успешно! Привет, {username}')
                else:
                    info['error'] = f'Регистрация разрешена с 18ти лет. Будем рады видеть вас через {18 - age} лет.'
            else:
                info['error'] = 'Пароли не совпадают.'
        else:
            info['error'] = 'Этот логин уже занят.'

    context = {'info': info}
    return render(request, 'fifth_task/registration_page.html', context)


