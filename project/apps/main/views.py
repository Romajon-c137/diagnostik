from django.shortcuts import render


def main(request):
    # to do list
    todolist = [
        {'id': 1, 'title': 'Задача 1', 'done': False},
        {'id': 2, 'title': 'Задача 2', 'done': True},
        {'id': 3, 'title': 'Задача 3', 'done': False},
        {'id': 4, 'title': 'Задача 4', 'done': True},
        {'id': 5, 'title': 'Задача 5', 'done': False},
    ]
    return render(request, 'main/index.html', {'name': 'World', 'list': todolist})



def services(request):
    return render(request, 'services/index.html')