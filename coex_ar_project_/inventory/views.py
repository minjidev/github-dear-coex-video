# views.py
from rest_framework import viewsets, filters

# Don't forget to import the models and serializers even if you haven't created them
from .serializers import InventorySerializer, ProductSerializer, ProductTypeSerializer, StoreSerializer, UserActionSerializer, UserActionRankingSerializer
from .models import Inventory, Product, ProductType, Store, UserAction
from django.db.models import Max
from django.db.models import Q, Sum, Case, When, IntegerField




# We create one ViewSet for each table we have at the moment
# We can customize this logic later

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class UserActionViewSet(viewsets.ModelViewSet):
    queryset = UserAction.objects.all()
    serializer_class = UserActionSerializer

class UserActionByUsernameViewSet(viewsets.ModelViewSet):
    serializer_class = UserActionSerializer

    def get_queryset(self):
        #This username we get from the url pattern, for example useraction/username/<username>/ where username will be the username
        username = self.kwargs['username']

        return UserAction.objects.filter(user=username)

class LatestUserActionViewSet(viewsets.ModelViewSet):
    serializer_class = UserActionSerializer

    def get_queryset(self):
        username = self.kwargs['username']

        #print(UserAction.objects.filter(user=username, action_type='LIKED' | action_type='CANCEL LIKE')).values('product__product_name','action_type', 'date_time').aggregate(Max('date_time')))


        #latest_like = UserAction.objects.filter(Q(user=username), Q(action_type='LIKED') | Q(action_type='CANCEL LIKE'))  
        latest_like = UserAction.objects.filter(Q(user=username), Q(action_type='LIKED') | Q(action_type='CANCEL LIKE')).group_by('product', 'store__store_name', 'action_type', 'date_time', 'user').order_by('product', '-date_time').distinct('product')
        latest_reserve = UserAction.objects.filter(Q(user=username), Q(action_type='RESERVED') | Q(action_type='CANCEL RESERVE')).group_by('product', 'store__store_name', 'action_type', 'date_time', 'user').order_by('product', '-date_time').distinct('product')
        final_queryset = latest_like.union(latest_reserve)
        return final_queryset


        #latest_like.values('product__name', 'store__name', 'action_type', 'date').aggregate(Max('date_time'))



class RankingActionsViewSet(viewsets.ModelViewSet):
    serializer_class = UserActionRankingSerializer

    def get_queryset(self) :
        storename = self.kwargs['storename']

        ranking_count = UserAction.objects.filter(Q(store=storename)).group_by('product').annotate(
            ranking_points=Sum(Case(
                When(action_type='CANCEL LIKE', then=-1),
                When(action_type='CANCEL RESERVE', then=-1),
                When(action_type='RESERVED', then=1),
                When(action_type='LIKED', then=1),
                default=0,
                output_field=IntegerField()
            ))
            ).order_by('-ranking_points')
        print(ranking_count)
        return ranking_count
        





        
       

