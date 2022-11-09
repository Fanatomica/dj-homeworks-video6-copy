from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def omlet(request):

    dish = 'omlet'
    choice = DATA[dish].copy()
    serve = int(request.GET.get('servings', 1))

    for ing, volume in choice.items():
        volume = volume * serve
        choice[ing] = volume
    context = {
      'recipe': choice, 'persons': serve, 'dish': 'омлет'
    }
    return render(request, 'calculator/index.html', context)


def pasta(request):

    dish = 'pasta'
    choice = DATA[dish].copy()
    serve = int(request.GET.get('servings', 1))

    for ing, volume in choice.items():
        volume = volume * serve
        choice[ing] = volume
    context = {
      'recipe': choice, 'persons': serve, 'dish': 'паста'
    }
    return render(request, 'calculator/index.html', context)


def buter(request):

    dish = 'buter'
    choice = DATA[dish].copy()
    serve = int(request.GET.get('servings', 1))

    for ing, volume in choice.items():
        volume = volume * serve
        choice[ing] = volume
    context = {
      'recipe': choice, 'persons': serve, 'dish': 'бутерброд'
    }
    return render(request, 'calculator/index.html', context)
