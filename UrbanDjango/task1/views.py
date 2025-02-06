from .models import Buyer, User, Game
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
# Create your views here.

def index1(request):
    title = "Организация праздников"
    offerta = "Заказать"
    cart = "Корзина"
    context = {
        "title": title,
        "offerta": offerta,
        "cart": cart,

    }
    return render(request, "index.html", context)

def offerta(request):
    title = "Список игр"
    # Получаем все игры из базы данных
    games = Game.objects.all()
    return render(request, 'offerta.html', {'games': games, 'title': title})  # Передаем коллекцию игр в контекст

def cart(request):
    title = "Корзина"
    back = "Вернуться обратно"
    context = {
        "title": title,
        "back": back,
    }
    return render(request, "cart.html", context)


existing_users = ["user1", "user2", "user3"]


def sign_up_by_django(request):
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Проверяем условия
            if password == repeat_password and age >= 18:
                # Проверяем, существует ли покупатель с таким именем
                if not Buyer.objects.filter(name=username).exists():
                    # Создаем нового покупателя
                    Buyer.objects.create(name=username, age=age)
                    return HttpResponse(f"Приветствуем, {username}!")  # Ответ при успешной регистрации
                else:
                    info['error'] = "Пользователь с таким именем уже существует."
            else:
                if age < 18:
                    info['error'] = "Вам должно быть не менее 18 лет."
                if password != repeat_password:
                    info['error'] = "Пароли не совпадают."

    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'registration_page.html', info)





