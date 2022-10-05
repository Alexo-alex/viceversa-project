from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['usertext']
    cnt_words = len(user_text.split(' '))
    reversed_text = user_text[::-1]
    context = {
        'user_text': user_text,
        'reversed_text': reversed_text,
        'cnt_words': cnt_words,
    }
    return render(request, 'reverse.html', context=context)
