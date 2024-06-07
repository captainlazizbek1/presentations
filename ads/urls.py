from django.urls import path
from ads.views import CreateAdsView, AdsListView, AdsDetailView, AdsByCategory, AdsBuyView

app_name = 'ads'
urlpatterns = [
    path('create/', CreateAdsView.as_view(), name='create_ads'),
    path('list/', AdsListView.as_view(), name='ads_list'),
    path('<int:pk>/', AdsDetailView.as_view(), name='ads_detail'),
    path('list/<str:name>/', AdsByCategory.as_view(), name="ads_by_category"),
    path('buying/<int:pk>/', AdsBuyView.as_view(), name='ads_buy'),
]






