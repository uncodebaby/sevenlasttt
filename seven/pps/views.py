from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'Lets talk!'},
    {'id': 2, 'name': 'Lets voice!'},
    {'id': 3, 'name': 'Lets share memes!'},
]


def homepage(request):
    context = {'rooms': rooms}
    return render(request, 'pps/home.html', context)


def roompage(request):
    return render(request, 'pps/    room.html')
