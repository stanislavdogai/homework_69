import json

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render

@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return JsonResponse({})
    return HttpResponseNotAllowed('Only GET request are allowed')


def add(request):
    data = json.loads(request.body)
    try:
        total = int(data['num1']) + int(data['num2'])
        return JsonResponse({'answer': str(total), 'element' : '+'})
    except ValueError:
        return JsonResponse({'error': 'input only numbers'}, status=400)

def subtract(request):
    data = json.loads(request.body)
    try:
        total = int(data['num1']) - int(data['num2'])
        return JsonResponse({'answer': str(total), 'element' : '-'})
    except ValueError:
        return JsonResponse({'error': 'input only numbers'}, status=400)

def multiply(request):
    data = json.loads(request.body)
    try:
        total = int(data['num1']) * int(data['num2'])
        return JsonResponse({'answer': str(total), 'element' : '*'})
    except ValueError:
        return JsonResponse({'error': 'input only numbers'}, status=400)

def divide(request):
    data = json.loads(request.body)
    try:
        if int(data['num1']) == 0 or int(data['num2']) == 0:
            return JsonResponse({'error': 'division by zero!'}, status=400)
        else:
            total = int(data['num1']) / int(data['num2'])
            return JsonResponse({'answer': str(total), 'element' : '/'})
    except ValueError:
        return JsonResponse({'error': 'input only numbers'}, status=400)

def math_logic(request):
    return render(request, 'index.html')