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
    if data['num1'].isdigit() and data['num2'].isdigit():
        total = int(data['num1']) + int(data['num2'])
        return JsonResponse({'answer': total, 'element' : '+'})
    else:
        return JsonResponse({'error': 'input only numbers'}, status=400)

def subtract(request):
    data = json.loads(request.body)
    if data['num1'].isdigit() and data['num2'].isdigit():
        total = int(data['num1']) - int(data['num2'])
        print(total)
        return JsonResponse({'answer': total, 'element' : '-'})
    else:
        return JsonResponse({'error': 'input only numbers'})

def multiply(request):
    if request.body:
        data = json.loads(request.body)
        if data['num1'].isdigit() and data['num2'].isdigit():
            total = int(data['num1']) * int(data['num2'])
            return JsonResponse({'answer': total, 'element' : '*'})
        else:
            return JsonResponse({'error': 'input only numbers'})

def divide(request):
    data = json.loads(request.body)
    if data['num1'].isdigit() and data['num2'].isdigit():
        if int(data['num1']) == 0 or int(data['num2']) == 0:
            return JsonResponse({'error': 'division by zero!'})
        else:
            total = int(data['num1']) / int(data['num2'])
            return JsonResponse({'answer': total, 'element' : '/'})
    else:
        return JsonResponse({'error': 'input only numbers'})

def math_logic(request):
    return render(request, 'index.html')