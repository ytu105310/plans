from django.urls import include, path
from rest_framework import routers
from plans.views.UserViewSet import UserViewSet
from plans.views.PlanViewSet import PlanViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'plans', PlanViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]