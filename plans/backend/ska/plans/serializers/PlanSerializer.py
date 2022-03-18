from plans.models import Plan
from rest_framework import serializers


class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = ['creator', 'Link']

