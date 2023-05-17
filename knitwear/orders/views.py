from django.shortcuts import render


def index(request):
    context = {
        'title': 'Зайцева',
        'products': [
            {
                'name': 'Шапка',
                'badge': 'NEW',
                'badge_color': 'bg-success',
                'img': 'static/img/carousel/1.jpg',
                'description': 'Вязанная шапка',
                'price': '3000',
                'sale': False,
            },
            {
                'name': 'Кофта для собаки',
                'badge': 'SALE',
                'badge_color': 'bg-danger',
                'img': 'static/img/carousel/2.jpg',
                'description': 'Кофта по индивидуальному размеру',
                'price': '5000',
                'sale': '3900',
            },
            {
                'name': 'Шарф',
                'badge': False,
                'badge_color': '',
                'img': 'static/img/carousel/3.jpg',
                'description': 'Вязанный шарф',
                'price': '2000',
                'sale': '1500',
            }
        ]
    }
    return render(request, 'index.html', context)




