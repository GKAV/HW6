
from django.shortcuts import render, redirect
from .forms import UserInfoForm
import json

from .models import UserInfo


def save_to_json(data):
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)

def index(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            user_data = list(UserInfo.objects.values())
            save_to_json(user_data)
            return redirect('index')
    else:
        form = UserInfoForm()

    return render(request, 'myapp/index.html', {'form': form, 'user_data': UserInfo.objects.all()})

