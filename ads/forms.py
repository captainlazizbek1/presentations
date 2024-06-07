from django import forms
from ads.models import Ads, Payment
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField


class CreateAdsForm(forms.ModelForm):

    class Meta:
        model = Ads
        fields = ['name', 'description', 'category', 'subject', 'price', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2}),
        }
        

class PaymentForm(forms.ModelForm):
    
    class Meta:
        model = Payment
        fields = ['cc_number', 'cc_expiry', 'cc_code']
        

