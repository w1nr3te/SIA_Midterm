from django.shortcuts import render, get_object_or_404
from .models import Pal, PlayerProfile

def index(request):
    pals = Pal.objects.all()
    context = {
        'pals': pals
    }
    return render(request, 'InvApp/Paldex_Showcase.html', context)


def profile_list(request):
    profiles = PlayerProfile.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'InvApp/profile_list.html', context)


def profile_detail(request, profile_id):
    profile = get_object_or_404(PlayerProfile, profile_id=profile_id)
    context = {
        'profile': profile
    }
    return render(request, 'InvApp/profile_detail.html', context)


def leaderboard(request):
    profiles = PlayerProfile.objects.all().order_by('-pals_captured')
    context = {
        'profiles': profiles
    }
    return render(request, 'InvApp/leaderboard.html', context)