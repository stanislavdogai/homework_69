from django.urls import path


from webapp.views import add, subtract, multiply, divide, math_logic, get_token_view

app_name = 'webapp'

urlpatterns = [
    path('add/', add, name='add'),
    path('subtract/', subtract, name='subtract'),
    path('multiply/', multiply, name='multiply'),
    path('divide/', divide, name='divide'),
    path('', math_logic, name='math_logic'),
    path('csrftoken/', get_token_view, name='get_token_view')
]
