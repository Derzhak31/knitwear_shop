menu = [
    {'title': 'Главная', 'url_name': 'index'},
    {'title': 'Каталог', 'url_name': 'products:index'},
    {'title': 'Оплата', 'url_name': 'payment'},
    {'title': 'Обратная связь', 'url_name': 'contacts'}
]


class DataMixin:
    def get_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context
