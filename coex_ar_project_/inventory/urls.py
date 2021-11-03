from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# Here you can add any url in which you will access the API
# For now we are adding urls for each table we are creating
# The urls will be accessed like this localhost:8000/api/inventory (example)
router.register(r'inventory', views.InventoryViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'producttype', views.ProductTypeViewSet)
router.register(r'store', views.StoreViewSet)
router.register(r'useraction', views.UserActionViewSet)
#router.register(r'useraction/(?P<username>.+)/$', views.UserActionByUsernameViewSet, basename = 'UserAction')
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path('useraction/customer/(?P<username>.+)/$', views.UserActionByUsernameViewSet.as_view({'get': 'list'})),
    re_path('useraction/actions/(?P<username>.+)/$', views.LatestUserActionViewSet.as_view({'get': 'list'})),
    re_path('useraction/ranking/(?P<storename>.+)/$', views.RankingActionsViewSet.as_view({'get': 'list'}))

    
]