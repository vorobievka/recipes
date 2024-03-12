import json

from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def hello(request, dish):
    servings = int(request.GET.get("servings", 1))
    print('a = ', dish)
    print(servings)
    # print(DATA.get('omlet'))
    print('data = ', DATA.get(dish))
    # context = {}
    # test = lambda x: x * 2, DATA.get('omlet') ???
    ingredients = {}
    for key in DATA.get(dish):
        ingredients[key] = DATA.get(dish)[key] * 2
    print('test = ', ingredients)
    print(DATA.get(dish))
    print(ingredients.get(dish))
    context = {
        # 'recipe': {
        #     'a': 2
        # }
        # 'recipe': DATA.get(a)
        'recipe': ingredients
    }
    test = {}
    # bad print(json.dumps(DATA.get('omlet')))
    # return HttpResponse('Hello from django')
    return render(request, 'calculator/index.html', context)
