from rest_framework import serializers
from .models import  Plan,Subscription

class PlanSerializer(serializers.ModelSerializer):
    # pass
    class Meta:
        model=Plan
        fields="__all__"
class SubscriptionSerializer(serializers.ModelSerializer):
    # pass
    class Meta:
        model=Subscription
        exclude=()
        fields="__all__"