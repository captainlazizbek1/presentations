from django.shortcuts import render, redirect, get_object_or_404
from django import views
from ads.forms import CreateAdsForm, PaymentForm
from ads.models import Ads, Category
from config.custom_permissions import OnlyLoggedSuperUser
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
class NotFoundView(views.View):
    def get(self, request):
        return render(request, 'notFound.html')


class CreateAdsView(OnlyLoggedSuperUser, views.View):
    
    def get(self,request):
        form = CreateAdsForm()
        context = {
            'form': form
        }
        return render(request, 'createAds.html',context)
    
    def post(self,request):
        form = CreateAdsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'The Ad has been created successfully')
            return redirect('ads:ads_list')
        else: 
            return HttpResponse('Form is not valid')


class AdsListView(views.View):

    def get(self, request):
        categories = Category.objects.all()
        ads = Ads.objects.all()
        search_query = request.GET.get('q','')
        if search_query:
            ads = ads.filter(name__icontains = search_query)
            if ads.count() == 0:
                messages.success(request,'Nothing found')
                ads = Ads.objects.all()
        context = {
            'ads': ads,
            'categories': categories,
            'search_query': search_query
        }
        return render(request,'adsList.html',context)
            

class AdsDetailView(views.View):

    def get(self, request, pk):
        ad = Ads.objects.get(id=pk)
        if ad:
            context = {
                'ad': ad
            }   
            return render(request, 'adsDetail.html', context)
        else:
            return redirect("not_found")
        

class AdsByCategory(views.View):

    def get(self, request, name):
        category = Category.objects.filter(name=name).first()
        ads = Ads.objects.filter(category=category)
        context = {
            'ads': ads,
            'category': category.name
        }
        return render(request, 'adsByCategory.html', context)
    

class AdsBuyView(views.View):
    def get(self,request, pk):
        form = PaymentForm()
        context = {
            'form': form
        }
        return render(request, 'adsBuy.html', context)
    
    def post(self, request, pk):
        form = PaymentForm(data=request.POST)
        ad = Ads.objects.get(id=pk)
        if form.is_valid() and ad:
            pass

    
