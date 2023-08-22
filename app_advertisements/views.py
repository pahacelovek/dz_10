from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm


def index(request):
    advertisements = Advertisement.objects.all()
    context = {"advertisements": advertisements}
    return render(request, "index.html", context)


def top_sellers(request):
    return render(request, "top-sellers.html")


def advertisement_post(request):
    if request.method == 'POST':
        f = AdvertisementForm(request.POST)
        valid = f.is_valid()
        if valid:
            f.save()
            return redirect('/')
        else:
            return HttpResponse(f'Произошла ошибка в форме<br>{f.errors}')
    else:
        form = AdvertisementForm()
        context = {"form": form}
        return render(request, "advertisement-post.html", context)
