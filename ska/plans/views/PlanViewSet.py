from rest_framework import viewsets
from rest_framework import permissions
from plans.serializers.PlanSerializer import PlanSerializer
from plans.models.Plan import Plan


class PlanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Plan.objects.all().order_by('date')
    serializer_class = PlanSerializer
    permission_classes = [permissions.IsAuthenticated]
