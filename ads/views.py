from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Ad, ExchangeProposal
from .forms import AdForm, ExchangeProposalForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.user.is_authenticated:
        return redirect('ads:ad_list')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('ads:ad_list')
    else:
        form = UserCreationForm()
    return render(request, 'ads/register.html', {'form': form})
@login_required
def ad_list(request):
    ads = Ad.objects.all()
    query = request.GET.get("q")
    category = request.GET.get("category")
    condition = request.GET.get("condition")

    if query:
        ads = ads.filter(title__icontains=query) | ads.filter(description__icontains=query)
    if category:
        ads = ads.filter(category__iexact=category)
    if condition:
        ads = ads.filter(condition__iexact=condition)

    return render(request, "ads/ad_list.html", {"ads": ads})
@login_required
def ad_detail(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    return render(request, "ads/ad_detail.html", {"ad": ad})

@login_required
def ad_create(request):
    if request.method == "POST":
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            return redirect("ads:ad_detail", pk=ad.pk)
    else:
        form = AdForm()
    return render(request, "ads/ad_form.html", {"form": form})

@login_required
def ad_edit(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    if ad.user != request.user:
        raise PermissionDenied
    if request.method == "POST":
        form = AdForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            return redirect("ads:ad_detail", pk=ad.pk)
    else:
        form = AdForm(instance=ad)
    return render(request, "ads/ad_form.html", {"form": form})

@login_required
def ad_delete(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    if ad.user != request.user:
        raise PermissionDenied
    ad.delete()
    return redirect("ads:ad_list")

@login_required
def proposal_create(request):
    if request.method == "POST":
        form = ExchangeProposalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ads:proposal_list")
    else:
        form = ExchangeProposalForm()
    return render(request, "ads/proposal_form.html", {"form": form})

@login_required
def proposal_list(request):
    proposals = ExchangeProposal.objects.all()
    return render(request, "ads/proposal_list.html", {"proposals": proposals})
