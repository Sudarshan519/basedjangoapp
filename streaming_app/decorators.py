from datetime import date
from rest_framework.permissions import BasePermission

from subscription.models import Subscription
class IsSubscribed(BasePermission):
        def has_permission(self, request, view):
            active_subscriptions=Subscription.objects.filter(user=request.user,end_date__gte=date.today()).all()
            return bool(request.user and active_subscriptions)