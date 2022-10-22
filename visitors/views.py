
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    # Зареєструє нового користувача.
    if request.method != 'POST':
        # Виводе пусту форму реєстрації.
        form = UserCreationForm()
    else:
        # Обробка заповненої форми
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('core:index')

    context = {'form': form}
    return render(request, 'visitors/register.html', context)
