from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import vk
# Create your views here.


def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    context = {}
    social = request.user.social_auth.get(provider='vk-oauth2')
    token = social.extra_data.get('access_token')
    session = vk.Session(access_token=token)
    vkapi = vk.API(session)
    friends = vkapi.friends.get(v='5.21', order='random', count=5, fields=['domain'])
    context.update({'friends': friends['items']})
    return render(request, 'home.html', context=context)
